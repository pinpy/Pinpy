from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# from .models import *

# Список для главного меню сайта.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Поддержать проект", 'url_name': 'support'},
        {'title': "Войти", 'url_name': 'sign_in'},
        {'title': "Зарегистрироваться", 'url_name': 'sign_up'},
        ]


# Главная страница.
def home(request):
    # Обработка шаблона главной страницы.
    return render(request, 'notes/home.html', {'menu': menu, 'title': 'Главная страница'})


# Оснавная страница.
def main(request):
    return render(request, 'notes/main.html', {'menu': menu, 'title': 'Pinpy'})


# О сайте.
def about(request):
    return render(request, 'notes/about.html', {'menu': menu, 'title': 'О сайте'})


# Контакты.
def contacts(request):
    return render(request, 'notes/contact.html', {'menu': menu, 'title': 'Контакты'})


# Поддержать нас.
def support_us(request):
    return render(request, 'notes/support.html', {'menu': menu, 'title': 'Поддержать нас'})


# Войти.
def sign_in(request):
    return HttpResponse('<h1>Войти</h1>')


# Зарегистрироваться.
def sign_up(request):
    return HttpResponse('<h1>Зарегистрироваться</h1>')


# Обработка исключения 404.
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def bad_request(request, exception):  # Невозможно обработать запрос.
# def permission_denied(request, exception):  # Доступ запрещен.
# def server_error(request, exception):  # Ошибка сервера.
