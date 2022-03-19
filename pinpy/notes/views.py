from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView


# from .models import *

# Главная страница.
def home(request):
    # Обработка шаблона главной страницы.
    return render(request, 'notes/home.html', {'title': 'Главная страница'})


# Оснавная страница.
def main(request):
    return render(request, 'notes/main.html', {'title': 'Pinpy'})


# О сайте.
def about(request):
    return render(request, 'notes/about.html', {'title': 'О сайте'})


# Контакты.
def contacts(request):
    return render(request, 'notes/contact.html', {'title': 'Контакты'})


# Поддержать нас.
def support_us(request):
    return render(request, 'notes/support.html', {'title': 'Поддержать нас'})


# Войти.
def sign_in(request):
    return render(request, 'notes/sign_in.html', {'title': 'Войти'})


# Зарегистрироваться.
def sign_up(request):
    return render(request, 'notes/sign_up.html', {'title': 'Зарегистрироваться'})


# Добавить заметку.
def add_note(request):
    if request.method == 'POST':  # Если данные ранее были заполнены, то форма заполняется этими данными.
        form = AddNoteForm(request.POST, request.FILES)
        if form.is_valid():  # Если проверка прошла, то полученные данные добавляются в бд.
            form.save()
            return redirect('home')
    else:
        form = AddNoteForm()
    return render(request, 'notes/add_note.html', {'form': form, 'title': 'Добавить заметку'})


# Посмотреть заметку.
def show_note(request, note_slug, factory_id):
    note = get_object_or_404(Notes, slug=note_slug, factory_id=factory_id)
    return render(request, 'notes/note.html', context={'note': note, 'title': note.title})


# Обработка исключения 404.
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def bad_request(request, exception):  # Невозможно обработать запрос.
# def permission_denied(request, exception):  # Доступ запрещен.
# def server_error(request, exception):  # Ошибка сервера.


'''Не трогать
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'notes/sign_up.html'
    success_url = reverse_lazy('login')
'''
