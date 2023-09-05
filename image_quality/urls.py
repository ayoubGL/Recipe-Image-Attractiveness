
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
    path('ghs_fk', views.ghs_fk, name='ghs_fk'),
    path('rate_salad', views.rate_salad,name='rate_salad'),
    path('rate_pasta', views.rate_pasta,name='rate_pasta'),
    path('rate_snacks', views.rate_snacks,name='rate_snacks'),
    path('rate_dissert', views.rate_dissert,name='rate_dissert'),
    path('rate_recipes',views.rate_recipes, name='rate_recipes'),
    path('thank_u', views.thank_u,name='thank_u'),

]