# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('demo.views',
    (r'^$', 'demo'),
    (r'^demo1/$', 'demo1'),
)
