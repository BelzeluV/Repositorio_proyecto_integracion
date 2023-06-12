from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Appi.models import *

class UserForm(UserCreationForm):
    
    RUT                 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: 123456789-0", "oninput": "checkRut(this)","maxlength": "11"}))
    nombre_real         = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: Juan Perez"}))
    nacimiento          = forms.DateField(widget=forms.DateInput(format = ('%Y-%m-%d'), attrs = {"type": "date", "class": "form-control-sm"}))
    email               = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: Correo@Ejemplo.com"}))
    telefono            = forms.CharField(widget = forms.TextInput(attrs={"style": "text-transform: capitalize", "class": "form-control form-control-sm", "pattern": "[0-9]+", "placeholder": "(9) 1234 5678 "}))
    Direccion           = forms.CharField(widget = forms.TextInput(attrs={"style": "text-transform: capitalize", "class": "form-control form-control-sm","placeholder": "Ingrese su dirección"}))
    #foto_de_Usuario     = forms.FileField(widget = forms.FileInput(attrs={"class": "form-control form-control-sm"}))


    class Meta:
        model           = get_user_model()
        fields          = 'username','password1','password2','nombre_real','RUT','nacimiento','email','genero','telefono','Direccion','comuna',#'foto_de_Usuario',
        

