from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect

from .forms import *
from .models import *
from .utils import Mixin
from django.urls import reverse_lazy  # Формирование маршрута по его имени.
from django.views.generic import ListView, DetailView, CreateView, FormView


# Главная страница.
class Home(Mixin, ListView):  # Родительские классы обрабатываются по порядку записи.
    model = Notes  # Атрибут model связывает представление с моделью Notes.
    template_name = 'notes/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):  # Передает шаблону статические файлы.
        context = super().get_context_data(**kwargs)  # context ссылается на словарь, где сохраняются данные.
        context['title'] = 'Pinpy'  # В методе класса Mixin указавается параметр title.
        return context  # Объединение словарей.


# Добавить заметку.
class AddNote(LoginRequiredMixin, CreateView):  # Ограничение доступа к странице для неавторизованных пользователей.
    form_class = AddNoteForm  # Атрибут form_class связывает представление с классом формы AddPostForm.
    template_name = 'notes/add_note.html'
    context_object_name = 'form'  # Указываем имя, по которому будут доступны данные из модели.
    success_url = reverse_lazy('home')  # Перенаправляет на указанную ссылку при добавлении записи.

    # login_url = reverse_lazy('sign_in')  # Перенаправляет на указанную ссылку незарегистрированного пользователя.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить заметку'
        return context


# Зарегистрироваться.
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'notes/sign_up.html'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    # Метод вызывается при успешной отправке данных формы (POSTed).
    def form_valid(self, form):
        user = form.save()  # Добавление пользователя в БД.
        login(self.request, user)  # Вход в систему.
        return redirect('home')


# Войти.
class SignIn(LoginView):
    form_class = SignInForm
    template_name = 'notes/sign_in.html'
    context_object_name = 'form'
    no_cookies = False
    account_disabled = False
    invalid_login = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        return context

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
        return super().form_valid(form)


# Посмотреть заметку.
class ShowNote(DetailView):
    model = Notes
    template_name = 'notes/note.html'
    context_object_name = 'note'
    allow_empty = False  # Генерация исключения 404, если заметок нет.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.user.get_username() + '/' + str(context['note'])  # "Имя пользователя/заметка".
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


# Обратная связь.
class Feedback(FormView):
    form_class = FeedbackForm
    template_name = 'notes/feedback.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обратная связь'
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# Поддержать нас.
class SupportUs(ListView):
    model = Notes
    template_name = 'notes/support.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поддержать нас'
        return context


# Выход
def logout_user(request):
    logout(request)
    return redirect('home')


# Профиль.
class Profile(DetailView):
    model = User
    template_name = 'notes/profile.html'
    slug_field = "username"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.user.get_username()
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
