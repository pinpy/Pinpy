from django.apps import AppConfig


# Используется для конфигурации всего приложения.
class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
    verbose_name = 'Приложение Notes'
