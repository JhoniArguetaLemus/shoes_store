from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.products, name='home'),
    path('second', views.second, name='second')
]