from django import template
from core.models import LeftMenu1, LeftMenu2, LeftMenu3, IndexAuthor, Banner1, Banner2, Banner3, Chat, Shows

register = template.Library()

@register.inclusion_tag('templatetags/left_menu.html')
def show_left_menu():
    return {
    	'menu1' : LeftMenu1.objects.all(),
    	'menu2' : LeftMenu2.objects.all(),
    	'menu3' : LeftMenu3.objects.all(),
    }

@register.inclusion_tag('templatetags/index_author.html')
def show_index_author():
    return {
        'index_author' : IndexAuthor.objects.all()[:1],
    }

@register.inclusion_tag('templatetags/chat.html')
def show_index_chat():
    return {
        'chat' : Chat.objects.all()[:1],
    }

@register.inclusion_tag('templatetags/banners.html')
def show_banners():
    return {
        'banner1' : Banner1.objects.all()[:1],
        'banner2' : Banner2.objects.all()[:1],
        'banner3' : Banner3.objects.all()[:1],
    }

@register.inclusion_tag('templatetags/shows.html')
def show_shows():
    return {
        'shows' : Shows.objects.all()[:5],
    }