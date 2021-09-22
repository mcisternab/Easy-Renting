from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse, response
from django.contrib import messages
from .forms import UCFWithEmail, AFWithEmail


def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "departamento/index.html")
    # En otro caso redireccionamos al login
    return redirect('/login')


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UCFWithEmail()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UCFWithEmail(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()
            messages.success(request, f'usuario {user.username} creado')

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/index')

    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/index')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def principal(request):
    return render(request, "departamento/principal.html")

def index(request):
    return render(request, "departamento/index.html")

def dptos(request):
    return render(request, "departamento/dptos.html")

def dptos2(request):
    return render(request, "departamento/dptos2.html")

def servicios(request):
    return render(request, "departamento/servicios.html")
