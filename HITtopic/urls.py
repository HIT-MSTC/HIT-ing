from django.conf.urls import url
from HITtopic import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),
    url(r'^create_topic/$',views.create_topic)
    
    ]
