"""bootproto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from bootproto.core.views import main_view, main_view3, main_view4

urlpatterns = [
    url(r'^bootstrap-prototype/main1/$', main_view, name='main'),
    url(r'^bootstrap-prototype/main2/$', TemplateView.as_view(template_name='core/main2.html')),
    url(r'^bootstrap-prototype/main3/$', main_view3, name='main3'),
    url(r'^bootstrap-prototype/main4/$', main_view4, name='main4'),
    url(r'^admin/', include(admin.site.urls)),
]
