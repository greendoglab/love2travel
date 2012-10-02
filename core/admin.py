# -*- coding: utf-8 -*-
from core.models import LeftMenu1, LeftMenu2, LeftMenu3, Banner1, Banner2, Banner3, IndexAuthor, Chat, Shows
from django.contrib import admin
from sorl.thumbnail import default

ADMIN_THUMBS_SIZE = '100x100'

class LeftMenu1Admin(admin.ModelAdmin):
    list_per_page = 10

class LeftMenu2Admin(admin.ModelAdmin):
    list_per_page = 10

class LeftMenu3Admin(admin.ModelAdmin):
    list_per_page = 10

admin.site.register(LeftMenu1, LeftMenu1Admin)
admin.site.register(LeftMenu2, LeftMenu2Admin)
admin.site.register(LeftMenu3, LeftMenu3Admin)
admin.site.register(IndexAuthor)
admin.site.register(Chat)
admin.site.register(Banner1)
admin.site.register(Banner2)
admin.site.register(Banner3)
admin.site.register(Shows)