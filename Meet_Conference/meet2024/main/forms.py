from django import forms
from .models import Registration, Event

class RegistrationForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'phone', 'events']