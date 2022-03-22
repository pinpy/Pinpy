from django import forms
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

    # def form_valid(self, form):
    #    form.instance.created_by = self.request.user
    #    return super().form_valid(form)
