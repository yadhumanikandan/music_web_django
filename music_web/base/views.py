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
    if request.method == "POST":
        search = request.POST.get("search")
        data = Scale.objects.filter(name__contains=search)
        return render(request, 'base/all_cards.html', {'data': data})
    
    else:
        data = Scale.objects.all()
        return render(request, 'base/all_cards.html', {'data': data})


def show_result(request, id):
    data = Scale.objects.filter(id=id)
    
    return render(request, 'base/scale.html', {'data': data})  # change to showing the scale details page