from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Scale, Chord
from.forms import ScaleForm, ChordForm

# Create your views here.

music_admin = "yadhu"

@login_required
def admin_dashboard(request):
    if request.user.username == music_admin:
        return render(request, 'music_admin/dashboard.html')
    
    else:
        return HttpResponse("not allowed!!!")
    

@login_required
def add_scale(request):

    if request.user.username == music_admin:

        if request.method == 'POST':
            
            name = request.POST.get('name')

            if not Scale.objects.filter(name=name):
                form = ScaleForm(request.POST, request.FILES)
        
                if form.is_valid():
                    form.save()
                    return redirect('base:show_scales')
                
            else:
                messages.error(request, 'Scale alredy exists in database.')
                return redirect('music_admin:add_scale')
        else:
            form = ScaleForm()
        return render(request, 'music_admin/add_scale.html', {'form': form})
    
    else:
        return HttpResponse("not allowed!!!")
    


@login_required
def add_chord(request):

    if request.user.username == music_admin:

        if request.method == 'POST':
            
            name = request.POST.get('name')

            if not Chord.objects.filter(name=name):
                form = ChordForm(request.POST, request.FILES)
        
                if form.is_valid():
                    form.save()
                    return redirect('base:show_chords')
                
            else:
                messages.error(request, 'Chord alredy exists in database.')
                return redirect('music_admin:add_chord')
        else:
            form = ChordForm()
        return render(request, 'music_admin/add_chord.html', {'form': form})
    
    else:
        return HttpResponse("not allowed!!!")
