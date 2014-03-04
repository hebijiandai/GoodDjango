# coding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blog import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'GoodDjango.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/custom/', views.custom_view),
                       url(r'^admin/nonexist/',views.nonexist_view),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^select2/', include('django_select2.urls')),
                       )
