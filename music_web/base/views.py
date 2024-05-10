from django.shortcuts import render, redirect
from django.http import HttpResponse
from music_admin.models import Scale

# Create your views here.


def home(request):
    return render(request, 'base/home.html')



def account(request):
    if request.user.is_authenticated:
        return render(request, "base/account.html")
    
    else:
        return redirect('authenticat:signin')


def show_scales(request):
    data = Scale.objects.all()
    return render(request, 'base/display_data.html', {'data': data})