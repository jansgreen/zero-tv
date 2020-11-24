from django.urls import path
from . import views
from .webhooks import my_webhook_view


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<str:order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout/', views.cache_checkout, name='cache_checkout'),
    path('checkout/', views.checkout, name='checkout'),
    path('webhooks/', my_webhook_view, name='webhooks'),

]