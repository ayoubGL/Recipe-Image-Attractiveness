
from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls import handler404, handler500


app_name = "image_quality"

urlpatterns = [
    path ('', views.home, name='home'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('rate_salad', views.rate_salad,name='rate_salad')
]