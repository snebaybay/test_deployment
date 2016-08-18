from django.conf.urls import url, include
from . import views    

urlpatterns = [             
    url(r'^$', views.index),
    url(r'^users$', views.increment) ,
    url(r'^reset$', views.reset) 
]
