import re
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ]
    )
    delivery_address = forms.CharField(required=False)  # Исправление опечатки
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ]
    )

    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]

        # Разрешить символ "+" в начале строки и цифры после него
        pattern = re.compile(r"^\+\d{12}$")
        if not pattern.match(data):
            raise forms.ValidationError(
                "Невірний формат номеру. Номер повинен починатися з '+' та має містити 12 цифр"
            )

        return data
