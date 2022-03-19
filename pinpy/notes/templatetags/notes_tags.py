# Шаблонны теги.
from django import template
from notes.models import *

# Экземпляр класса Library, через который происходит регистрация собственных шаблонных тегов.
register = template.Library()

'''
# Пример простого тега, возвращающего колекцию данных.
# Функция выполняется при вызове тега из шаблона. 
# Декоратор связывает функцию с тегом. 
@register.simple_tag(name='getcats')  # name задает имя тегу,на которое можно ссылаться. 
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

# Пример включающего тега, формирующего фрагмент html страницы.
@register.inclusion_tag('notes/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()  # Чтение всех рубрик из БД. 
    else:
        cats = Category.objects.order_by(sort)
   
    return {"cats": cats, "cat_selected": cat_selected}  # Возврат словаря с данными. 

'''
