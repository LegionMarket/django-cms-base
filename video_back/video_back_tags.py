from django import template

register = template.Library()

@register.filters
def image(value):
    return value + 1
