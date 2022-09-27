from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def text_to_link(value):
    return mark_safe(f"<a href='https://yandex.ru/search/?text={value}'>{value}</a>")
