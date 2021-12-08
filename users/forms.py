from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from departamento.models import Contacto, Arriendo, Pasajero, Pago

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

class ArriendoForm(forms.ModelForm):

    class Meta:
        model = Arriendo
        fields = ["nombre_cliente","apellido_cliente","email_cliente","usuario_cliente","departamento","zona","cantidad_personas","fecha_entrada","fecha_salida","precio","precio_final"]

class PasajeroForm(forms.ModelForm):

    class Meta:
        model = Pasajero
        fields = ["nombre_cliente","rut_pasajero","nombre_completo"]

class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago
        fields = ["orden_compra","tipo_tarjeta","numero_tarjeta","titular_tarjeta","expira","cvc","usuario"]