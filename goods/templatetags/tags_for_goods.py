from django import template
from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():  # Чтоб не прописываать в каждом views отображение categories
    return Categories.objects.all()
