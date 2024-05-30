from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

# Створюємо файл спецільно для валідації. AuthenticationForm створений якраз для цього, перевірка вже зареєстрвоаних
from users.models import User


class UserSign_in_Form(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User


class UserSign_on_Form(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class Profile_Form(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )
