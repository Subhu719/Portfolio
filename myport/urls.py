from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexpage, name="index"),
    path('port',views.portfolio, name="port"),
    path('service',views.service, name="service"),
    path('contactform', views.contactform, name='contactform')
]
    