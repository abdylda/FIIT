"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
import landing

urlpatterns = [
    path('', views.test),
    path('kabinet/', views.kabinet, name='kabinet'),
    path('Category/', views.category, name='Category'),
    path('NalichiTehniki/', views.nalichiTehniki, name='NalichiTehniki'),
    path('KlassInjener/', views.klassInjener, name='KlassInjener'),
    path('Ingener/', views.Ingener, name='Ingener'),
    path('KlassMebel/', views.klassMebel, name='KlassMebel'),
    path('kabinetti/koruu/<int:id>', views.kabinet_koruu, name='kabinetti_koruu'),


]
