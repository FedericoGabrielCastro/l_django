from django import template
from ..models import Projects

register=template.Library()

@register.simple_tag
def total_projects():
    return Projects.objects.count()