from django.contrib import admin

from .models import *


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'photo', 'time_create',
                    'time_update')  # Список полей, отображаемых в admin панели.
    list_display_links = ('id', 'title')  # Поля, по которым можно перейти на соответсвующее содержимое.
    search_fields = ('title', 'content')  # По каким полям производится поиск информации. 
    # list_editable = ('is_published',)  # Редактируемые поля.
    list_filter = ('time_create',)  # Поля, по которым можно фильтровать содержимое модели.
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение поля slug по полю title.


admin.site.register(Notes, NotesAdmin)  # Регистрация модели для admin понели.
