# -*- coding: utf-8 -*-
from partners.models import Partner
from django.contrib import admin

class PartnerAdmin(admin.ModelAdmin):
    list_per_page = 15
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'body')
        }),
    )

admin.site.register(Partner, PartnerAdmin)