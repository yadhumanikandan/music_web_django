from django import forms
from .models import Scale, Chord
 
 
class ScaleForm(forms.ModelForm):
 
    class Meta:
        model = Scale
        fields = ['name', 'scale', 'discription', 'keyboard_image', 'guitar_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'scale': forms.TextInput(attrs={'class': 'form-control'}),
            'discription': forms.Textarea(attrs={'class': 'form-control'}),

        }


class ChordForm(forms.ModelForm):
 
    class Meta:
        model = Chord
        fields = ['name', 'discription', 'keyboard_image', 'guitar_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'scale': forms.TextInput(attrs={'class': 'form-control'}),
            'discription': forms.Textarea(attrs={'class': 'form-control'}),

        }