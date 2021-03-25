from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from table.forms import *
from table.models import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

#----------------------users view--------------------------------


class RegisterView(View):
    def get(self, request):
        user_form = RegisterUserForm()
        return render(request, 'register.html', {'user_form': user_form})

    @transaction.atomic
    def post(self, request):
        form = RegisterUserForm(request.POST)
        if not form.is_valid():
            return redirect('/register')
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            messages.error(request, 'Login zajęty. Wybierz inny.')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.info(request, 'Dodano nowego użytkwnika.')
        return redirect('login')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

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


class CategorySelectionView(View):
    def get(self, request):
        # user = request.user
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