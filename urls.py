from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.index'),
    (r'^category/(?P<slug>[^\.]+)/$', 'core.views.view_category'),
    (r'^tour/(?P<slug>[^\.]+)/$', 'core.views.view_tour'),
    (r'^blog/(?P<slug>[^\.]+)/$', 'core.views.view_blog'),
    (r'^page/(?P<slug>[^\.]+)/$', 'core.views.view_page'),
    (r'^partners/$', 'core.views.view_partners'),
    (r'^tours/$', 'core.views.view_tours'),
    (r'^order/$', 'feedback.views.feedback'),
    (r'^thanks/$', 'feedback.views.thanks'),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)