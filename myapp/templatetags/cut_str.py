from django import template

register=template.Library()

@register.filter(name="cut_str")
def cut_str(value, arg):
    return value[0:arg]