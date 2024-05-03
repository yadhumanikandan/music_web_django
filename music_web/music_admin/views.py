from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Scale
from.forms import ScaleForm

# Create your views here.


@login_required
def admin_dashboard(request):
    return render(request, 'dashboard.html')
    

@login_required
def add_scale(request):
 
    if request.method == 'POST':
        form = ScaleForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('show_db')
    else:
        form = ScaleForm()
    return render(request, 'add_scale.html', {'form': form})
    

@login_required
def show_db(request):
    data = Scale.objects.all()
    return render(request, 'display_data.html', {'data': data})
