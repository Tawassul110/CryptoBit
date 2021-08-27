from django import template

register = template.Library()

@register.filter
def multiply(number, number1):
    return float(number) * float(number1)