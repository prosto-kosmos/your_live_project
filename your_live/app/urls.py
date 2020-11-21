from django.urls import path
from . import views

urlpatterns = [
    path('', views.Start_view.as_view(), name='start_url'),
    path('main/', views.Main_view.as_view(), name='main_url'),
]