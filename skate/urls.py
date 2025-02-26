from django.urls import path
from .views import index, about, contact, shop, skating

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('skating/', skating, name='skating'),
]