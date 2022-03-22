import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from unidecode import unidecode


class Notes(models.Model):
    title = models.CharField(max_length=127, verbose_name='Заголовок')
    slug = models.SlugField(blank=True, max_length=127, db_index=True, verbose_name='URL')  # Понятная человеку URL.
    content = models.TextField(blank=True, verbose_name='Содержимое')
    photo = models.ImageField(blank=True, upload_to='photos/%y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    factory_id = models.UUIDField(default=uuid.uuid4)  # uuid - уникальный идентификатор (чтобы ссылки не совпадали).

    # is_published = models.BooleanField(default=True, verbose_name='Публикация')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)

    # Выводит title при запросе к элементам бд.
    def __str__(self):
        return self.title

    # Используется модулями django по умолчанию для построения ссылок.
    def get_absolute_url(self):
        return reverse('note', kwargs={'slug': self.slug, 'factory_id': self.factory_id})

    # slug заполняется автоматически, если запись не была создана (нету id), инче slug остается прежним.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.title))  # unidecode переводит многие символы в нужную форму.
        return super().save(*args, **kwargs)

    # Используется admin панелью для настройки/отображения модели. 
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['time_create', 'title']  # Порядок сортировки.
