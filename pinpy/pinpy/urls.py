from django.contrib import admin
from django.urls import path, include

from notes.views import page_not_found

'''Указываем файл со списком url из приложения notes
(для независимости приложений).  
'''
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('notes.urls')),
]

# Присвоение функции обработки исключения ошибке 404.
handler404 = page_not_found

# handler400 – невозможно обработать запрос.
# handler403 – доступ запрещен.
# handler500 – ошибка сервера.
