from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    items = Products.objects.all()
    return render(request, 'index.html', {'products': items})


def about(request):
    return HttpResponse(render(request, 'about.html'))
