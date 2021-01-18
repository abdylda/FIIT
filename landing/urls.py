from django.contrib.auth import login
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
import landing
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.test, name='index'),
    path('kabinet/', views.kabinet, name='kabinet'),
    path('Category/', views.category, name='Category'),
    path('NalichiTehniki/', views.nalichiTehniki, name='NalichiTehniki'),
    path('KlassInjener/', views.klassInjener, name='KlassInjener'),
    path('Ingener/', views.Ingener, name='Ingener'),
    path('KlassMebel/', views.klassMebel, name='KlassMebel'),
    path('kabinetti/koruu/<int:id>', views.kabinet_koruu, name='kabinetti_koruu'),
    path('categoryny/koruu/<int:id>', views.category_koruu, name='category_koruu'),
    path('sostoyanieny/koruu/<str:filter>', views.sostoyanieny_koruu, name='sostoyanieny_koruu'),


]
