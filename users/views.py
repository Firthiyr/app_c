from django.shortcuts import render
from django.contrib import auth
from users.forms import UserSign_in_Form
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def sign_in(request):
    if request.method == "POST":
        form = UserSign_in_Form(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserSign_in_Form()

    context = {"title": "Home - Авторизація", "form": form}
    return render(request, "users/sign_in.html", context)


def sign_up(request):

    context = {
        "title": "Home - Реєстрація",
    }
    return render(request, "users/sign_up.html", context)


def profile(request):

    context = {
        "title": "Home - Профіль",
    }
    return render(request, "users/profile.html", context)


def logout(request): ...
