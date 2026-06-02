from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def intcomma_latin(value):
    try:
        return "{:,}".format(int(value))
    except (ValueError, TypeError):
        return value

@register.filter
def rial_to_toman(value):
    try:
        toman = int(float(value)) // 10
        return intcomma(toman)
    except (ValueError, TypeError):
        return value
