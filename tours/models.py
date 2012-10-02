# -*-coding: utf-8-*-
from django.db import models
from django.contrib.sites.models import Site
from blog.models import Category, Post
import re
import datetime
from sorl.thumbnail import ImageField

class TourCategory(Category):

	def get_absolute_url(self):
		return 'http://%s/tour/category/%s/' % (Site.objects.get_current().domain, self.slug)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Туры: Категории"

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

	def __unicode__(self): 
		return self.title
        
	class Meta:
		ordering = ['-date']
		verbose_name_plural = "Туры: Запись"