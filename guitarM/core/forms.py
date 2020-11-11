from django import forms
from django.forms import ModelForm
from .models import Instrumento
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class InstrumentoForm(ModelForm):
    
    marca = forms.CharField(min_length=2, max_length=200)
    modelo = forms.CharField(min_length=2, max_length=200)

    class Meta:
       model = Instrumento
       fields = ['marca','modelo','mantencion','tipo','fecha_entrega']  

       widgets = {
           'fecha_entrega': forms.SelectDateWidget(years=range(2020,2021))
        }

    def clean_fecha_entrega(self):
        fecha = self.cleaned_data['fecha_entrega'] 

        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser mayor a la fecha de hoy")

        return fecha

class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']   


