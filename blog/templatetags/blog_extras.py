from django import template
from blog.models import TourPost, Category

register = template.Library()

@register.inclusion_tag('templatetags/hot_tours.html')
def show_hot_tours():
    return {
    	'hot_tours' : TourPost.objects.filter(hot=True)[:3]
    }

@register.inclusion_tag('templatetags/show_cat_menu.html')
def show_cat_menu():
	return {
		'menu' : Category.objects.all(),
	}