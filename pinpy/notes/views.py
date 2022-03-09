from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Главная страница.
def home(request):
    return HttpResponse('<h1>Главная страница</h1>')


# Обработка исключения 404.
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def bad_request(request, exception):  # Невозможно обработать запрос.
# def permission_denied(request, exception):  # Доступ запрещен.
# def server_error(request, exception):  # Ошибка сервера.
