from django.conf.urls import url,patterns
from orphanages import views

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^about/?$',views.about),
        url(r'^contact/?$',views.contact),
        url(r'^orphanages/?$',views.orphanages),
        url(r'^orphanages/(?P<url>\w+)/?$',views.orphanage),
        url(r'^oldagehomes/?$',views.oldagehomes),
        url(r'^oldagehomes/(?P<url>\w+)/?$',views.oldagehome),
        url(r'^birthdaydonation/?$',views.birthdaydonation),
        )
