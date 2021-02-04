from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import CreateView, FormView

from Documents.models import Document
from landing.forms import LoginForm
from landing.models import Kabinet, Category, NalichiTehniki, Engineer, Mebel
from test_project import settings


@login_required
def test(request):
    return render(request, 'test.html')


@login_required
def kabinet(request):
    kabinetter = Kabinet.objects.all()
    return render(request, 'kabinet.html', {'kabinetter': kabinetter})


@login_required
def category(request):
    Categoryler = Category.objects.all()
    return render(request, 'Category.html', {'Categoryler': Categoryler})


@login_required
def nalichiTehniki(request):
    NalichiTehnikiler = NalichiTehniki.objects.all()
    return render(request, 'NalichiTehniki.html', {'NalichiTehnikiler': NalichiTehnikiler})





@login_required
def klassInjener(request):
    KlassInjenerler = Engineer.objects.all()
    return render(request, 'KlassInjener.html', {'KlassInjenerler': KlassInjenerler})


@login_required
def kabinet_koruu(request, id):
    buiumdar = NalichiTehniki.objects.filter(Kabinet=id)
    return render(request, 'NalichiTehniki.html', {'NalichiTehnikiler': buiumdar})


def Ingener(request):
    Ingenerler = Engineer.objects.all()
    return render(request, 'Ingener.html', {'Ingenerler': Ingenerler})


@login_required
def klassMebel(request):
    KlassMebeler = Mebel.objects.all()
    return render(request, 'KlassMebel.html', {'KlassMebeler': KlassMebeler})


def category_koruu(request, id):
    buiumdar = NalichiTehniki.objects.filter(category=id)
    return render(request, 'NalichiTehniki.html', {'NalichiTehnikiler': buiumdar})


@login_required
def sostoyanieny_koruu(request, filter):
    buiumdar = NalichiTehniki.objects.filter(sostoyanie=filter)
    return render(request, 'NalichiTehniki.html', {'NalichiTehnikiler': buiumdar})


@login_required
def document(request):
    Documenter = Document.objects.all()
    return render(request, 'Document.html', {'Documenter': Documenter})

def upload_document(reguest):
    return render(reguest, 'upload_list.html')

def upload_document(reguest):
    return render(reguest, 'upload_document.html')