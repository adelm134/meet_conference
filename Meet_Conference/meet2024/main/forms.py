from django import forms
from .models import Registration, Event
from django.core.exceptions import ValidationError
import re

class RegistrationForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'phone', 'events']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Registration.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже зарегистрирован.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise ValidationError("Телефонный номер должен содержать только цифры и может начинаться с '+'.")
        return phone

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[a-zA-Zа-яА-Я]+$', first_name):
            raise ValidationError("Имя должно содержать только буквы.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[a-zA-Zа-яА-Я]+$', last_name):
            raise ValidationError("Фамилия должна содержать только буквы.")
        return last_name