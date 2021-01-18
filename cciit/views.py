from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import CreateView, FormView
from landing.forms import LoginForm
from cciit.models import Available_techniques, Categories, Cabinet, Engineers
from test_project import settings



@login_required
def available_techniques(request):
    Available_techniquesler = Available_techniques.objects.all()
    return render(request, 'Available_techniques.html', {'Available_techniquesler': Available_techniquesler})


@login_required
def sostoyani_koruu(request, filter):
    buiumdar = Available_techniques.objects.filter(sostoyani=filter)
    return render(request, 'Available_techniques.html', {'Available_techniquesler': buiumdar})


@login_required
def сategories(request):
    Categoriesler = Categories.objects.all()
    return render(request, 'Categories.html', {'Categoriesler': Categoriesler})


def сategories_koruu(request, id):
    material = Available_techniques.objects.filter(Categories=id)
    return render(request, 'Available_techniques.html', {'Available_techniquesler': material})


@login_required
def Cabinetnew(request):
    Cabinetter = Cabinet.objects.all()
    return render(request, 'Cabinet.html', {'Cabinetter': Cabinetter})


@login_required
def сabinet_koruu(request, id):
    material = Available_techniques.objects.filter(Cabinet=id)
    return render(request, 'Available_techniques.html', {'Available_techniquesler': material})


@login_required
def klassInjenernew(request):
    Engineersler = Engineers.objects.all()
    return render(request, 'klassInjeneroitok.html', {'Engineersler': Engineersler})