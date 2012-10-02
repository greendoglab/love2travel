# -*-coding: utf-8-*-
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
import re
import datetime
from sorl.thumbnail import ImageField

class Category(models.Model):
    title = models.CharField('Заголовок', max_length=500, help_text="Заголовок")
    slug = models.SlugField('URL', unique=True, help_text="Если не автоматически, Например: Some_tour, some-tour")
    seo_descritption = models.TextField('SEO Description', help_text="Описание (Для браузеров)", blank=True)
    seo_keywords = models.TextField('SEO Keywords', help_text="Ключевые слова (Для браузеров)", blank=True)

    def get_absolute_url(self):
        return 'http://%s/category/%s/' % (Site.objects.get_current().domain, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"

class Post(models.Model):
    slug = models.SlugField("URL", unique=True, help_text='Если не автоматически, Например: Some_tour, some-tour')
    title = models.CharField("Заголовок", max_length=500, help_text="Заголовок")
    seo_descritption = models.TextField(help_text="Описание (Для браузеров)", blank=True)
    seo_keywords = models.TextField(help_text="Ключевые слова (Для браузеров)", blank=True)
    body = models.TextField("Контент", help_text="Ипользуется разметка Textile")
    post_preview = ImageField("Картинка превью к записи", upload_to='posts', blank=True, help_text="Картинка превью поста(декор)")
    date = models.DateTimeField("Дата публикации", default=datetime.datetime.now)

    category = models.ManyToManyField('blog.Category', help_text="Категория")

    def start_date(self):
        return self.tourpost.start_date

    def end_date(self):
        return self.tourpost.end_date

    def get_absolute_url(self):
        try:
            return self.blogpost.get_absolute_url()
        except ObjectDoesNotExist:
            return self.tourpost.get_absolute_url()

    def get_body(self):
        return re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)

    def get_description(self):
        body_desc = re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)
        return body_desc.partition("<!--more-->")[0]

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Блог: Запись"

class BlogPost(Post):

    def get_absolute_url(self):
        return 'http://%s/blog/%s/' % (Site.objects.get_current().domain, self.slug)

    def get_body(self):
        return re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)

    def get_description(self):
        body_desc = re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)
        return body_desc.partition("<!--more-->")[0]

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Запись: блог"

class TourPost(Post):
    hot = models.BooleanField("Горящий тур", default=False, help_text="Заголовок")
    start_date = models.DateField("Дата начала тура", blank=True, null=True)
    end_date = models.DateField("Дата конца тура", blank=True, null=True)

    def get_absolute_url(self):
        return 'http://%s/tour/%s/' % (Site.objects.get_current().domain, self.slug)

    def get_body(self):
        return re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)

    def get_description(self):
        body_desc = re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)
        return body_desc.partition("<!--more-->")[0]

    def get_hot_decription(self):
        body_desc = re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r'', self.body)
        return body_desc.partition("<!--more-->")[0]

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Запись: тур"