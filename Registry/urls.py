from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Registry.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg_query/$', 'Registry.views.reg_query', name='reg_query'),
    url(r'^reg_connect/$', 'Registry.views.reg_connect'),
    url(r'^reg_remove/$', 'Registry.views.reg_remove'),
    url(r'^reg/$', 'Registry.views.reg'),
    url(r'^regp/$', 'Registry.views.regp'),
    url(r'^reg_config/$', 'Registry.views.reg_config'),
    url(r'^reg_becomeguide/$', 'Registry.views.reg_becomeguide'),
    url(r'^reg_notification/$', 'Registry.views.reg_notification'),
    url(r'^reg_setNotification/$', 'Registry.views.reg_setNotification'),
    url(r'^reg_getNotification/$', 'Registry.views.reg_getNotification'),
    url(r'^reg_delNotification/$', 'Registry.views.reg_delNotification'),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'Registry.views.login', name='login'),
    url(r'^logout/$', 'Registry.views.logout', name='logout'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
