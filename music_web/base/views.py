from django.shortcuts import render, redirect
from django.http import HttpResponse
from music_admin.models import Scale

# Create your views here.


def home(request):
    return render(request, 'home.html')


def show_scales(request):
    data = Scale.objects.all()
    return render(request, 'display_data.html', {'data': data})