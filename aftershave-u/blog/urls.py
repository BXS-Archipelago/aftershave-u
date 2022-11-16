
from django.urls import path

from . import views


urlpatterns = [
  path('search/', views.search, name='search'),
  path('<slug:brands_slug>/<slug:slug>/', views.detail, name='post_detail'),      
  path('<slug:slug>/', views.brands, name='brands_detail'),   
 ]
