# -*-coding: utf-8-*-
from django.db import models
from django.contrib.sites.models import Site
import datetime
from sorl.thumbnail import ImageField

class Partner(models.Model):

    image = ImageField("Картинка", upload_to='images', help_text="Каритинка, .jpg, .png")
    name = models.CharField("Имя", max_length=500, help_text="Заголовок")
    body = models.TextField("Описание", help_text="Ипользуется разметка Textile")

    date = models.DateTimeField("Дата буликации", default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Партнер"