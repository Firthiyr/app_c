from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Створюємо файл спецільно для валідації. AuthenticationForm створений якраз для цього, перевірка вже зареєстрвоаних
from users.models import User


class UserSign_in_Form(AuthenticationForm):
    # username = forms.CharField()
    # password = forms.CharField()

    class Meta:
        model = User
