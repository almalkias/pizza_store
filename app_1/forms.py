from django import forms
from .models import Pizza

class Pizza_Form(forms.ModelForm):
    class Meta:
        model=Pizza
        fields = '__all__'
