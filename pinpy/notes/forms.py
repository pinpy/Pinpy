from django import forms
from .models import *


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'photo', 'is_published']  # Отображаемые поля.
        widgets = {  # Описывает стили оформления для каждого поля.
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10, 'placeholder': 'Напишите что-нибудь'}),
        }

        #def form_valid(self, form):
        #    form.instance.created_by = self.request.user
        #    return super().form_valid(form)