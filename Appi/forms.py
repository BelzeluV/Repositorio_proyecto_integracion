from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Appi.models import *

class UserForm(UserCreationForm):
    username            = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: el_queso_bakán","maxlength": "11",'required': 'required'}))
    password1           = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese su contraseña','required': 'required'}))
    password2           = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Repita su contraseña','required': 'required'}))
    first_name          = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: Pedro","maxlength": "40",'required': 'required'}))
    last_name           = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: Riquelme Sandoval","maxlength": "40",'required': 'required'}))
    email               = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: Correo@Ejemplo.com",'required': 'required'}))
    RUT                 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "ej: 123456789-0", "oninput": "checkRut(this)","maxlength": "11",'required': 'required'}))
    nacimiento          = forms.DateField(widget=forms.DateInput(format = ('%Y-%m-%d'), attrs = {"type": "date", "class": "form-control form-control-sm",'required': 'required'}))
    telefono            = forms.CharField(widget = forms.TextInput(attrs={"style": "text-transform: capitalize", "class": "form-control form-control-sm", "pattern": "[0-9]+", "placeholder": "(9) 1234 5678 ",'required': 'required'}))
    Direccion           = forms.CharField(widget = forms.TextInput(attrs={"style": "text-transform: capitalize", "class": "form-control form-control-sm","placeholder": "Ingrese su dirección",'required': 'required'}))
    foto_de_Usuario     = forms.FileField(widget = forms.FileInput(attrs={"class": "form-control form-control-sm","onchange":"previewImage(event)","accept":"image/*"}))


    class Meta:
        model           = get_user_model()
        fields          = 'first_name','last_name','username','password1','password2','RUT','nacimiento','email','genero','telefono','Direccion','comuna','foto_de_Usuario', 