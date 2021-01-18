from django.contrib.auth import login
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
import landing
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('Available_techniques/', views.available_techniques, name='Available_techniques'),
    path('sostoyani/koruu/<str:filter>', views.sostoyani_koruu, name='sostoyani_koruu'),
    path('Categories/', views.сategories, name='Categories'),
    path('categoriesyny/koruu/<int:id>', views.сategories_koruu, name='categories_koruu'),
    path('Cabinet/', views.Cabinetnew, name='Cabinet'),
    path('cabinetti/koruu/<int:id>', views.сabinet_koruu, name='сabinet_koruu'),
    path('Engineers/', views.klassInjenernew, name='Engineers'),
]
