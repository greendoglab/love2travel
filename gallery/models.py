# -*-coding: utf-8-*-
from django.db import models
from blog.models import Post
import os.path
from sorl.thumbnail import ImageField

class GalleryImage(models.Model):
    image = ImageField("Картинка", upload_to='images', help_text="Каритинка, .jpg, .png")
    title = models.CharField("Нащвание картинки", max_length=500, help_text="Заголовок", blank=True)
    parent = models.ManyToManyField('blog.Post', null=True, help_text="Родительская страница", blank=True)

    def get_title(self):
        return self.title if self.title else u'No name'

    class Meta:
        verbose_name_plural = "Картинки"