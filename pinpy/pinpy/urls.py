from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from notes.views import page_not_found
from pinpy import settings

'''Указываем файл со списком url из приложения notes
(для независимости приложений).  
'''
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('notes.urls')),
    path('captcha/', include('captcha.urls')),
]

# Передача загруженных файлов приложению в процессе отладки.
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Статические файлы.

# Присваение функции обработки исключения ошибки 404.
handler404 = page_not_found

# handler400 – невозможно обработать запрос.
# handler403 – доступ запрещен.
# handler500 – ошибка сервера.
