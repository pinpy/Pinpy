from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


# Главная страница.
class Home(ListView):
    model = Notes  # Атрибут model связывает представление с моделью Notes.
    template_name = 'notes/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):  # Передает шаблону статические файлы.
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'  # context ссылается на словарь, где сохраняются данные.
        return context


# Оснавная страница.
class Main(ListView):
    model = Notes
    template_name = 'notes/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pinpy'
        return context


# О сайте.
class About(ListView):
    model = Notes
    template_name = 'notes/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О сайте'
        return context


# Контакты.
class Contacts(ListView):
    model = Notes
    template_name = 'notes/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


# Поддержать нас.
class SupportUs(ListView):
    model = Notes
    template_name = 'notes/support.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поддержать нас'
        return context


# Войти.
class SignIn(ListView):
    model = Notes
    template_name = 'notes/sign_in.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        return context


# Зарегистрироваться.
class SignUp(ListView):
    model = Notes
    template_name = 'notes/sign_up.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Зарегистрироваться'
        return context


# Добавить заметку.
class AddNote(CreateView):
    form_class = AddNoteForm  # Атрибут form_class связывает представление с классом формы AddPostForm.
    template_name = 'notes/add_note.html'
    context_object_name = 'form'  # Указываем имя, по которому будут доступны данные из модели.
    success_url = reverse_lazy('home')  # Перенаправляет на указанную ссылку при добавлении записи.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить заметку'
        return context


# Посмотреть заметку.
class ShowNote(DetailView):
    model = Notes
    template_name = 'notes/note.html'
    context_object_name = 'note'
    allow_empty = False  # Генерация исключения 404, если заметок нет.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['note']
        return context


# Обработка исключения 404.
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def bad_request(request, exception):
    return HttpResponseNotFound('<h1>Невозможно обработать запрос</h1>')


def permission_denied(request, exception):
    return HttpResponseNotFound('<h1>Доступ запрещен</h1>')


def server_error(request, exception):
    return HttpResponseNotFound('<h1>Ошибка сервера</h1>')


'''Не трогать
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'notes/sign_up.html'
    success_url = reverse_lazy('login')
'''
