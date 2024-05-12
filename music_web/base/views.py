from django.shortcuts import render, redirect
from django.http import HttpResponse
from music_admin.models import Scale
from base.models import NewsLetter
from django.contrib import messages

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
        return render(request, 'base/all_cards.html', {'data': data, 'search': search})
    
    else:
        data = Scale.objects.all()
        return render(request, 'base/all_cards.html', {'data': data})


def show_result(request, id):
    data = Scale.objects.filter(id=id)
    
    return render(request, 'base/scale.html', {'data': data}) 


def news_letter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if NewsLetter.objects.filter(email=email):
            messages.error(request, "Email already registerd!!")

            return redirect("base:home")
        
        newsletter = NewsLetter.objects.create(email=email)
        newsletter.save()


        messages.info(request, "Subscribed to Newsletter :)")

        return redirect('base:home')
    
    else:
        return redirect('base:home')