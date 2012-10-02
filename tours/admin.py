# -*- coding: utf-8 -*-
from blog.models import Category
from tours.models import TourCategory, TourPost
from mediastorage.models import ImageStorage
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_per_page = 25

class TourPostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_per_page = 15
	fieldsets = (
		(None, {
		    'fields': ('title', 'slug', 'category', 'date')
		}),
		('Инфо тура', {
		    'fields': ('hot', 'start_date', 'end_date')
		}),
		('Содержимое', {
		    'fields': ('post_preview', 'body')
		}),
		('СЕО', {
		    'fields': ('seo_descritption', 'seo_keywords')
		})
	)

admin.site.register(TourPost, TourPostAdmin)
admin.site.register(Category, CategoryAdmin)