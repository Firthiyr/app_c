from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import (
    login_required,
)  # Імпортуємо декоратор, щоб заборонити користувачам що не мають профілю, потрапляти на сторінку
from users.forms import UserSign_in_Form, UserSign_on_Form, Profile_Form
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
                messages.success(request, f"{username}, Ви увійшли до аккануту")
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
            messages.success(
                request,
                f"{user.username}, Ви успішно зареєструвалися і увійшли до аккануту",
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserSign_on_Form()

    context = {"title": "Home - Реєстрація", "form": form}
    return render(request, "users/sign_up.html", context)


@login_required  # декоратор, заборон. користувачам що не мають профілю, потрапляти на сторінку реєстрації (404)
def profile(request):
    if request.method == "POST":
        form = Profile_Form(
            data=request.POST,
            instance=request.user,
        )  # files=request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "Профіль успішно оновлено!")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = Profile_Form(instance=request.user)

    context = {"title": "Home - Профіль", "form": form}
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Ви вийшли з аккануту")
    auth.logout(request)
    return redirect(reverse("main:index"))
