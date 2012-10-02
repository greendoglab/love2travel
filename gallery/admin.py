# -*- coding: utf-8 -*-
from gallery.models import GalleryImage
from django.contrib import admin
from sorl.thumbnail import default

ADMIN_THUMBS_SIZE = '100x100'

class GalleryImageAdmin(admin.ModelAdmin):
    def image_display(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
        return '<img src="%s" width="%s" />' % (thumb.url, thumb.width)

    def original(self, obj):
        return obj.image.url

    filter_horizontal = ('parent',)

    image_display.allow_tags = True
    list_display = ('get_title', 'image_display')
    list_per_page = 10

admin.site.register(GalleryImage, GalleryImageAdmin)