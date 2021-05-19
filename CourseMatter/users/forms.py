from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries import countries
from django import forms
COUNTRY_CHOICES = tuple(countries)
from django.contrib.auth.models import User
# from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True)
    email = forms.EmailField
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("username","email","first_name", 'last_name', 'date_of_birth','country','password1','password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'


class CustomUserChangeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


