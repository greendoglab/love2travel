# -*- coding: utf-8 -*-
from pages.models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 15
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'date')
        }),
        ('Меню', {
            'fields': ('service', 'inmenu', 'parent')
        }),
        ('Содержимое', {
            'fields': ('body',)
        }),
        ('СЕО', {
            'fields': ('seo_descritption', 'seo_keywords')
        })
    )
    #change_form_template = '/templates/admin/change_form.html'
    # class Media:
    #   js = ['/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js']

admin.site.register(Page, PageAdmin)