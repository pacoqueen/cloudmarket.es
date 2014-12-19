# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from gifts import views

urlpatterns = patterns("",
                       # por ejemplo: /gifts/
                       url(r'^$', views.index, name = "index"),
                       # por ejemplo: /gifts/5
                       url(r'^(?P<gift_id>\d+)/$', views.detail, name = "detail"),
                       # por ejemplo: /gifts/5/mark
                       url(r'^(?P<gift_id>\d+)/mark/$', views.mark, name = "mark"),
                      )
