from django.urls import path
from . import views

urlpatterns=[
    path('products/', views.products, name='products'),
    path('second', views.second, name='second')
]