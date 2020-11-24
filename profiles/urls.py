from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('order_history', views.order_history, name='order_history'),

  
  ]