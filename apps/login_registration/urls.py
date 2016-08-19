from django.conf.urls import url, include
from . import views    

urlpatterns = [             
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^appointment$', views.success),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^logout$', views.logout)

]
