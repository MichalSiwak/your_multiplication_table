from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from table.forms import *
from table.models import *
from m1 import maths
import json
import pprint


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_name = request.user
            return render(request, 'index.html', {'user_name': user_name})
        else:
            return render(request, 'index.html')

    # def post(self, request):
    #     if 'logout' in request.POST:
    #         return redirect('logout')
    #     if 'login' in request.POST:
    #         return redirect('login')
    #     if 'register' in request.POST:
    #         return redirect('register')
    #     if 'user' in request.POST:
    #         return redirect('user')

#----------------------users view--------------------------------


class RegisterView(View):
    def get(self, request):
        form = RegisterUserForm()
        # form = LoginForm()
        register = True
        # print(request.path)
        # messages.info(request, 'Rejestracja przebiegła pomyślnie.')
        return render(request, 'register.html', {'form': form, 'register': register})

    @transaction.atomic
    def post(self, request):
        form = RegisterUserForm(request.POST)

        if not form.is_valid():
            return redirect('/register')

        if User.objects.filter(username=form.cleaned_data['username']).exists():
            messages.error(request, 'Login zajęty. Wybierz inny.')
            return redirect('/register')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        email = form.cleaned_data['email']
        # print(password)
        # print(repeat_password)

        if password != repeat_password:
            messages.error(request, 'Hasła muszą być takie same.')
            return redirect('/register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        ProfileParent.objects.create(user_id=user.id)
        messages.info(request, 'Rejestracja przebiegła pomyślnie.')
        return redirect('login')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        login = True
        # messages.info(request, 'Rejestracja przebiegła pomyślnie.')
        return render(request, 'login.html', {'form': form, 'login': login})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(** form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Błędny login lub hasło')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Nastąpił błąd. Skontaktuj sie z nami!!!')
            return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

#__________________________________________________________________________


class UserView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if User.objects.get(user_ptr_id=user.id).parent is True:
            is_parent = True
            user_name = User.objects.get(id=user.id)
            parent = ProfileParent.objects.get(user_id=user.id)
            kids = ProfileKid.objects.filter(parent_id=parent.id)

            return render(request, 'user.html', {'user_name': user_name, 'kids': kids,
                                                 'is_parent': is_parent})

        elif User.objects.get(user_ptr_id=user.id).parent is False:
            is_parent = False
            user_name = User.objects.get(id=user.id)
            kid = ProfileKid.objects.filter(user_id=user.id)
            image = f'{user.id}_pp.jpg'
            return render(request, 'user.html', {'user_name': user_name, 'is_parent': is_parent,
                                                 'kid': kid, 'image': image})


    def post(self, request):
        # print(request.POST)
        if request.POST.get('add') == 'edit':
            return redirect('edit_profile')
        if request.POST.get('add') == 'add':
            return redirect('new_kid')
        return redirect('new_kid')


class AddNewKidView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewKidForm()
        return render(request, 'new_kid.html', {'form': form})

    @transaction.atomic
    def post(self, request):

        form = NewKidForm(request.POST)
        if not form.is_valid():
            return redirect('new_kid')
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            messages.error(request, 'Login zajęty. Wybierz inny.')
        user = request.user
        parent = ProfileParent.objects.get(user_id=user.id)
        email = user.email
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=username, email=email, password=password, parent=False)
        user.save()
        ProfileKid.objects.create(parent_id=parent.id, points_counter=0, available_points=0, user_id=user.id)
        messages.info(request, 'Dodano nowego użytkwnika.')
        return redirect('login')


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        form = EditKidsProfileForm(initial={"username": user.username})
        return render(request, 'edit_profile.html', {'form': form})

    def post(self, request):
        myfile = request.FILES['profile_picture']
        username = request.POST.get('username')
        user = request.user
        fs = FileSystemStorage()
        picture_name = f"{user.id}_pp.jpg"
        fs.delete(picture_name)
        filename = fs.save(picture_name, myfile)
        fs.url(filename)
        User.objects.filter(id=user.id).update(username=username)
        ProfileKid.objects.filter(user_id=user.id).update(profile_picture=picture_name)
        return redirect('edit_profile')



# -------------------------------------------------

class CategorySelectionView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Categories.objects.all()
        return render(request, 'choice.html', {'categories': categories})

    def post(self, request):
        # user = request.user
        # user_id = user.id
        category = request.POST.get("category")
        if category == 'Historia':
            return redirect('history')
        elif category == 'Matematyka':
            return redirect('match')
        elif category == 'Biologia':
            return redirect('biology')
        else:
            return render(request, 'index.html')


class MatchView(View):
    def get(self, request):
        numb = maths.draw_number(2, 10)
        print(numb)
        form = None
        # return render(request, 'base.html', {'form': form})
        return HttpResponse("Matematyka."
                            "Strona w budowie")


class HistoryView(View):
    def get(self, request):
        return HttpResponse("Historia."
                            "Strona w budowie")


class BiologyView(View):
    def get(self, request):
        return HttpResponse("Biologia."
                            "Strona w budowie")


class TestView(View):

    def get(self, request, counter=5):
        maths.pairs_of_numbers = []
        counter = counter
        maths.draw_pars(counter)
        pairs_of_numbers = maths.pairs_of_numbers
        return render(request, 'test.html', {'pairs_of_numbers': pairs_of_numbers})

    def post(self, request):
        maths.data = []
        form = (request.POST)
        results = dict(form)['result']
        score_board = maths.checking_operations(maths.pairs_of_numbers, results)
        maths.exercise_points = maths.points(score_board)
        return redirect('test1')


class TestPointsView(View):
    def get(self, request):
        data = maths.data
        print(data)
        points = maths.exercise_points

        return render(request, 'test1.html', {'points': points, 'data': data})


