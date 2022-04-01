from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'photo']  # Отображаемые поля.
        widgets = {  # Описывает стили оформления для каждого поля.
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10, 'placeholder': 'Напишите что-нибудь'}),
        }

    # Валидатор.
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина заголовка не может превышать 128 символов')
        return title


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control rounded-4', 'placeholder': 'Введите логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control rounded-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control rounded-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    remember_me = forms.BooleanField(required=False)  # CheckboxInput.

