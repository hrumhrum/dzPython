from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', 'mainapp.views.index'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^login/$',  login, { "template_name": "mainapp/index.html" }),
    url(r'^organization/$', 'mainapp.views.organization'),
    url(r'^search/organization/$', 'mainapp.views.organization'),
	url(r'^search/$', 'mainapp.views.search'),
	url(r'^users_list/$', 'mainapp.views.users_list'),
	url(r'^search/users_list/$', 'mainapp.views.users_list'),
)