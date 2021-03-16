from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

