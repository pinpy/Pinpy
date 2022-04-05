from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),  # Главная страница.
    path('feedback/', Feedback.as_view(), name='feedback'),  # Обратная связь.
    path('support_us/', SupportUs.as_view(), name='support_us'),  # Поддержать нас.
    path('about/', About.as_view(), name='about'),  # О сайте.
    path('sign_in/', SignIn.as_view(), name='sign_in'),  # Войти.
    path('sign_up/', SignUp.as_view(), name='sign_up'),  # Зарегистрироваться.
    path('logout/', logout_user, name='logout'),  # Выйти.
    path('<slug:slug>/', Profile.as_view(), name='profile'),  # Профиль.
    path('main/', Main.as_view(), name='main'),  # Основная страница.
    path('add_note/', AddNote.as_view(), name='add_note'),  # Добавить заметку (временно).
    path('note/<slug:slug>/<uuid:factory_id>/', ShowNote.as_view(), name='note'),
]
