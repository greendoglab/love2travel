# -*-coding: utf-8-*-
from django.db import models
import os.path
from sorl.thumbnail import ImageField

class ImageStorage(models.Model):
    image = ImageField("Картинка", upload_to='images', help_text="Каритинка, .jpg, .png")
    title = models.CharField("Нащвание картинки", max_length=500, help_text="Заголовок", blank=True)

    def get_title(self):
        return self.title if self.title else u'No name'

    class Meta:
        verbose_name_plural = "Файлы: Картинки"

class FileStorage(models.Model):
    ufile = models.FileField("Файл", upload_to='files', help_text="Файл, к примеру .pdf или .rar, .zip")
    title = models.CharField("Название файла", max_length=500, help_text ="Заголовок", blank=True)

    def get_title(self):
        return self.title if self.title else u'No name'

    class Meta:
        verbose_name_plural = "Файлы: Разное(pdf, doc, etc..)"