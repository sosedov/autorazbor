from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorization, name='auth'),
    path('usercab', views.usercab, name='usercab'),
    path('search', views.search, name='search'),
    path('parts', views.parts, name='parts'),
    path('order', views.order, name='order')
]