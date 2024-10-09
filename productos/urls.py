from django.urls import path
from . import views

urlpatterns=[
    path('', views.products, name='home'),
    path('home/men', views.mens, name='mens'),
    path('home/women', views.women, name='women'),
    path('search/', views.buscar_productos, name='search_product'),
    path('search_men/', views.search_men_shoes, name='search_men_shoes')
]