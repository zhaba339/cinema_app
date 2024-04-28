from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'cinema/index.html')


def films(request):
    return render(request, 'cinema/today.html')


def soon(request):
    return render(request, 'cinema/soon.html')


def contacts(request):
    return render(request, 'cinema/contacts.html')

