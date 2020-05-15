from django.shortcuts import render

from landing.models import Kabinet, Category, NalichiTehniki, Engineer, Mebel


def test(request):
    return render(request, 'test.html')


def contact(request):
    return render(request, 'basic.html', {'content': ['dsdvsdvsdvsdv']})


def kabinet(request):
    kabinetter = Kabinet.objects.all()
    return render(request, 'kabinet.html', {'kabinetter': kabinetter})


def category(request):
    Categoryler = Category.objects.all()
    return render(request, 'Category.html', {'Categoryler': Categoryler})


def nalichiTehniki(request):
    NalichiTehnikiler = NalichiTehniki.objects.all()
    return render(request, 'NalichiTehniki.html', {'NalichiTehnikiler': NalichiTehnikiler})

def klassInjener(request):
    KlassInjenerler = Engineer.objects.all()
    return render(request, 'KlassInjener.html', {'KlassInjenerler': KlassInjenerler})


def kabinet_koruu(request, id):
    buiumdar = NalichiTehniki.objects.filter(Kabinet=id)
    return render(request, 'NalichiTehniki.html', {'NalichiTehnikiler': buiumdar})

def Ingener(request):
    return render(request, 'Ingener.html')

def klassMebel(request):
    KlassMebeler = Mebel.objects.all()
    return render(request, 'KlassMebel.html', {'KlassMebeler': KlassMebeler})
