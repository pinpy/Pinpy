from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),  # Главная страница.
    path('about/', about, name='about'),  # О сайте.
    path('contact/', contact, name='contact'),  # Обратная связь.
    path('support/', support, name='support'),  # Поддержать проект.
    path('sign_in/', sign_in, name='sign_in'),  # Войти.
    path('sign_up/', sign_up, name='sign_up'),  # Зарегистрироваться.
]
