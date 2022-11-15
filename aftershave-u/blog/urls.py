
from django.urls import path

from . import views


urlpatterns = [
   path('<slug:brands_slug>/<slug:slug>/>', views.detail, name='post_detail'),   
   path('<slug:slug>/', views.brands, name='brands_detail'),
   path('<slug:slug>/', views.creators, name='creators_detail'),
 ]
# path('<slug:creators_slug>/<slug:slug>/>', views.detail, name='post_detail'),