# -*-coding: utf-8-*-
from django.db import models
import os.path
from sorl.thumbnail import ImageField
import datetime

class IndexAuthor(models.Model):
    text = models.TextField("Контент", help_text="Ипользуется разметка Textile")

    name = u'Об авторе'
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Об авторе: главная страница"

class Chat(models.Model):
    text = models.TextField("Контент", help_text="Ипользуется разметка Textile")

    name = u'Чат'
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Код чата"

class Banner1(models.Model):
    date = models.DateTimeField("Дата публикации", default=datetime.datetime.now)
    banner = ImageField("Иконка", upload_to='images', help_text="Каритинка, .jpg, .png")
    name = models.CharField("Название", max_length=500, help_text="Название пункта")
    link = models.CharField("Ссылка", max_length=500, help_text="Ссылка на рубрику в блог или тур. Например: /blog/news/ или /tours/hot/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Баннер 1 для главной страницы"

class Banner2(models.Model):
    date = models.DateTimeField("Дата публикации", default=datetime.datetime.now)
    banner = ImageField("Иконка", upload_to='images', help_text="Каритинка, .jpg, .png")
    name = models.CharField("Название", max_length=500, help_text="Название пункта")
    link = models.CharField("Ссылка", max_length=500, help_text="Ссылка на рубрику в блог или тур. Например: /blog/news/ или /tours/hot/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Баннер 2 для главной страницы"

class Banner3(models.Model):
    date = models.DateTimeField("Дата публикации", default=datetime.datetime.now)
    banner = ImageField("Иконка", upload_to='images', help_text="Каритинка, .jpg, .png")
    name = models.CharField("Название", max_length=500, help_text="Название пункта")
    link = models.CharField("Ссылка", max_length=500, help_text="Ссылка на рубрику в блог или тур. Например: /blog/news/ или /tours/hot/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Баннер 3 для главной страницы"

class LeftMenu1(models.Model):
    icon = models.CharField("Ииконка", max_length=500, help_text="Буква, соответсвующая разделу.")
    name = models.CharField("Название", max_length=500, help_text="Название пункта")
    link = models.CharField("Ссылка", max_length=500, help_text="Ссылка на рубрику в блог или тур. Например: /blog/news/ или /tours/hot/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Левое меню: секция 1"

class LeftMenu2(models.Model):
    icon = models.CharField("Ииконка", max_length=500, help_text="Буква, соответсвующая разделу.")
    name = models.CharField("Название", max_length=500, help_text="Название пункта")
    link = models.CharField("Ссылка", max_length=500, help_text="Ссылка на рубрику в блог или тур. Например: /blog/news/ или /tours/hot/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Левое меню: секция 2"

class LeftMenu3(models.Model):
    icon = models.CharField("Ииконка", max_length=500, help_text="Буква, соответсвующая разделу.")
    name = models.CharField("Название", max_length=500, help_text="Название пункта")
    link = models.CharField("Ссылка", max_length=500, help_text="Ссылка на рубрику в блог или тур. Например: /blog/news/ или /tours/hot/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Левое меню: секция 3"

class Shows(models.Model):
    image = ImageField("Картинка", upload_to='images', help_text="Каритинка, .jpg, .png")
    name = models.CharField("Название", max_length=500, help_text="Имя")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Декор фотография в шапку"