from django.shortcuts import render
from django.contrib import auth
from users.forms import UserSign_in_Form, UserSign_on_Form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

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
    if request.method == "POST":
        form = UserSign_on_Form(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserSign_on_Form()

    context = {"title": "Home - Реєстрація", "form": form}
    return render(request, "users/sign_up.html", context)


def profile(request):

    context = {
        "title": "Home - Профіль",
    }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))
