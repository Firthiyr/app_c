from django.shortcuts import render

# Create your views here.


def sign_in(request):

    context = {
        "title": "Home - Авторизація",
    }
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
