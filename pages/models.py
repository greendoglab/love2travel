# -*-coding: utf-8-*-
from django.db import models
from django.contrib.sites.models import Site
import re
import datetime

class Page(models.Model):
    inmenu = models.BooleanField("В меню", default=False, help_text="Эта страница материалов?")
    service = models.BooleanField("Услуги", default=False, help_text="Эта страница Услуг?")
    slug = models.SlugField("URL", help_text="Если не автоматически, Например: Some_tour, some-tour", unique=True)
    title = models.CharField("Заголовок", max_length=500, help_text="Заголовок")
    seo_descritption = models.TextField("SEO Description", help_text="Описание (Для браузеров)", blank=True)
    seo_keywords = models.TextField("SEO Keywords", help_text="Ключевые слова (Для браузеров)", blank=True)
    body = models.TextField("Контент", help_text="Ипользуется разметка Textile")

    parent = models.ForeignKey('pages.Page', null=True, help_text="Родительская страница", blank=True)

    date = models.DateTimeField("Дата буликации", default=datetime.datetime.now)

    def get_absolute_url(self):
        return 'http://%s/page/%s/' % (Site.objects.get_current().domain, self.slug)

    def get_body(self):
        return re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)

    def get_description(self):
        body_desc = re.sub(r'!(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', r"""<figure class="fig-image"><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.body)
        return body_desc.partition("<!--more-->")[0]

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Страницы сайта"