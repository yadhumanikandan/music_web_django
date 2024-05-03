from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Scales

# Create your views here.


@login_required
def admin_dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def add_scale(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        scale = request.POST.get("scale")
        discription = request.POST.get("discription")

        return HttpResponse(name+ " " +scale+ " " +discription)

    else:
        return render(request, 'add_scale.html')