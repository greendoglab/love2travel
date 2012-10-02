# -*- coding: utf-8 -*-
from mediastorage.models import ImageStorage, FileStorage
from django.contrib import admin
from sorl.thumbnail import default

ADMIN_THUMBS_SIZE = '100x100'
SITE_SIZE = '740x740'
SMALL_SIZE = '250x250'

class ImageStorageAdmin(admin.ModelAdmin):
    def image_display(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
        return '<img src="%s" width="%s" />' % (thumb.url, thumb.width)

    def post(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, SITE_SIZE)
        return thumb.url

    def small(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, SMALL_SIZE)
        return thumb.url

    def original(self, obj):
        return obj.image.url

    image_display.allow_tags = True
    list_display = ('get_title', 'image_display', 'post', 'small', 'original')
    list_per_page = 10

class FileStorageAdmin(admin.ModelAdmin):
    def get_url(self, obj):
        return obj.ufile.url

    list_display = ('get_title', 'get_url')
    list_per_page = 20

admin.site.register(ImageStorage, ImageStorageAdmin)
admin.site.register(FileStorage, FileStorageAdmin)