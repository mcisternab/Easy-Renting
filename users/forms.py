from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from departamento.models import Contacto

# Extendemos del original


class AFWithEmail(AuthenticationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.Field(label="Nombre usuario")

    class Meta:
        model = User
        fields = ["username", "password"]

# Extendemos del original


class UCFWithEmail(UserCreationForm):
    # Establecemos que el campo username es tipo email y el nombre
    username = forms.Field(label="Nombre usuario")

    class Meta:
        model = User
        fields = ["username","password1", "password2","first_name","last_name","email"]

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre","email","zona","mensaje"]

