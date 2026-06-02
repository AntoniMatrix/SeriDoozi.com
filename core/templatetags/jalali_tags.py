from django import template
import jdatetime

register = template.Library()

@register.filter
def to_jalali(value, format='%Y/%m/%d'):
    return jdatetime.datetime.fromgregorian(datetime=value).strftime(format)
