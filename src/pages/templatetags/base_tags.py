from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("pages/category.html")
def category():
    return {
        "category": Category.objects.filter(CategoryStatus=True),
    }

@register.inclusion_tag("pages/popularpost.html")
def popularpost():
    pass