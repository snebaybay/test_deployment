from django.conf.urls import url, include
from . import views    

urlpatterns = [             
    url(r'^$', views.index),
    url(r'^process$', views.create),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
]
