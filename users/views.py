from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import (
    login_required,
)  # Імпортуємо декоратор, щоб заборонити користувачам що не мають профілю, потрапляти на сторінку
from carts.models import Cart
from users.forms import UserSign_in_Form, UserSign_on_Form, Profile_Form
from django.http import HttpResponseRedirect
from django.urls import reverse
from orders.models import Order, OrderItem
from django.db.models import Prefetch

# Create your views here.


def sign_in(request):
    if request.method == "POST":
        form = UserSign_in_Form(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Ви увійшли до аккануту")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))

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

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

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

    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        )
        .order_by("-id")
    )

    context = {"title": "Home - Профіль", "form": form, "orders": orders}
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Ви вийшли з аккануту")
    auth.logout(request)
    return redirect(reverse("main:index"))


def users_cart(request):
    return render(request, "users/users_cart.html")
