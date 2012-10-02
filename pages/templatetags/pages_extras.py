from django import template
from pages.models import Page

register = template.Library()

@register.inclusion_tag('templatetags/page_menu.html')
def show_menu():
    return {
        'menu' : Page.objects.filter(inmenu=True),
    }

@register.inclusion_tag('templatetags/show_menu_service.html')
def show_menu_service():
  return {
      'menu' : Page.objects.filter(service=True),
  }

@register.inclusion_tag('templatetags/show_footer_menu.html')
def show_footer_menu():
    return {
        'menu1' : Page.objects.filter(inmenu=True).exclude(service=True).order_by('title'),
        # 'menu2' : Page.objects.filter(service=True),
    }