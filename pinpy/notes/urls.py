from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),  # Главная страница.
    path('contacts/', contacts, name='contact'),  # Контакты.
    path('support_us/', support_us, name='support_us'),  # Поддержать нас.
    path('about/', about, name='about'),  # О сайте.
    path('sign_in/', sign_in, name='sign_in'),  # Войти.
    path('sign_up/', sign_up, name='sign_up'),  # Зарегистрироваться.
    path('main/', main, name='main'),  # Основная страница.
    path('add_note/', add_note, name='add_note'),  # Добавить заметку (временно).
    path('note/<slug:note_slug>/<uuid:factory_id>/', show_note, name='note'),
]
