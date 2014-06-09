from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', 'mainapp.views.index'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^login/$',  login, { "template_name": "mainapp/index.html" }),
)