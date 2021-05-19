import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'sdfasdfasdf'})


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()-+=_')
    if request.GET.get('special'):
        characters.extend('12345679890')

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'the_password': the_password})
