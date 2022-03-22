from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),  # Главная страница.
    path('contacts/', Contacts.as_view(), name='contact'),  # Контакты.
    path('support_us/', SupportUs.as_view(), name='support_us'),  # Поддержать нас.
    path('about/', About.as_view(), name='about'),  # О сайте.
    path('sign_in/', SignIn.as_view(), name='sign_in'),  # Войти.
    path('sign_up/', SignUp.as_view(), name='sign_up'),  # Зарегистрироваться.
    path('main/', Main.as_view(), name='main'),  # Основная страница.
    path('add_note/', AddNote.as_view(), name='add_note'),  # Добавить заметку (временно).
    path('note/<slug:slug>/<uuid:factory_id>/', ShowNote.as_view(), name='note'),
]
