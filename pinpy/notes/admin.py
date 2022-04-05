from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'get_html_photo', 'time_create',
                    'time_update')  # Список полей, отображаемых в admin панели.
    list_display_links = ('id', 'title')  # Поля, по которым можно перейти на соответсвующее содержимое.
    search_fields = ('title', 'content')  # По каким полям производится поиск информации. 
    # list_editable = ('is_published',)  # Редактируемые поля.
    list_filter = ('time_create',)  # Поля, по которым можно фильтровать содержимое модели.
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение поля slug по полю title.
    fields = ('title', 'slug', 'content', 'photo', 'get_html_photo', 'time_create', 'time_update',
              'factory_id')  # Порядок и список редактируемых полей в форме редактирования.
    readonly_fields = ('time_create', 'time_update', 'factory_id', 'get_html_photo')  # Не редактируемые поля.
    save_on_top = True  # Добавление верхней панели для управления записью.

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')
        else:
            return "Нет фото"

    get_html_photo.short_description = 'Миниатюра'


admin.site.register(Notes, NotesAdmin)  # Регистрация модели для admin понели.
