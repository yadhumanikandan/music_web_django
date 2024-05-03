from django import forms
from .models import Scale
 
 
class ScaleForm(forms.ModelForm):
 
    class Meta:
        model = Scale
        fields = ['name', 'scale', 'discription', 'scale_img']