from django import template
from tours.models import TourPost

register = template.Library()

@register.inclusion_tag('templatetags/hot_tours.html')
def show_hot_tours():
    return {
    	'post' : TourPost.objects.all(),
    }