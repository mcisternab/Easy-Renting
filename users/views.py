from django.core import paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse, response
from django.contrib import messages
from django.views.generic.base import TemplateView
from .forms import UCFWithEmail, AFWithEmail
from django.core.paginator import Paginator
from django.http import Http404
from departamento.models import Departamento, Servicio, Zona , Transporte
from django.db.models import Q
import datetime

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
            messages.success(request, f'Bienvenid@ {user.username}, ya eres parte de Easy Renting')
            

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/index')
        else:
          messages.error(request, 'Usuario ya existente')
          

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
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')

        else:
             messages.error(request, 'Los datos no son válidos')

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

def cuenta(request):
    return render(request, "departamento/cuenta.html")

def dptos(request):
    busqueda = request.GET.get("buscar")
    departamentos = Departamento.objects.all()

    page = request.GET.get('page', 1)

    if busqueda:
        departamentos = Departamento.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(zona__nombre__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(departamentos, 9)
        departamentos = paginator.page(page)
    except:
        raise response.Http404

    data = {
        'entity': departamentos,
        'paginator': paginator

    }

    return render(request, "departamento/dptos.html", data)

def listadoServicios(request):
    busqueda = request.GET.get("buscarServicio")
    servicios = Servicio.objects.all()

    page = request.GET.get('page', 1)

    if busqueda:
        servicios = Servicio.objects.filter(
            Q(precio__icontains = busqueda) |
            Q(zona__nombre__icontains = busqueda) |
            Q(departamento__nombre__icontains = busqueda) |
            Q(tipo__tipo__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(servicios, 4)
        servicios = paginator.page(page)
    except:
        raise response.Http404

    data = {
        'entity': servicios,
        'paginator': paginator
    }

    return render(request, "departamento/listadoServicios.html", data)

def arrendar(request):
    now = datetime.datetime.now()
    zonas = Zona.objects.all()
    departamentos = Departamento.objects.all()

    data = {
        'zonas': zonas,
        'departamentos': departamentos,

    }

    return render(request, "departamento/arrendar.html", data)

def servicios(request):
    return render(request, "departamento/servicios.html")

def transporte(request):
    busqueda = request.GET.get("buscarTransporte")
    transportes = Transporte.objects.all()

    page = request.GET.get('page', 1)

    if busqueda:
        transportes = Transporte.objects.filter(
            Q(nombreConductor__icontains = busqueda) |
            Q(departamento__nombre__icontains = busqueda) |
            Q(zona__nombre__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(transportes, 4)
        transportes = paginator.page(page)
    except:
        raise response.Http404

    data = {
        'entity': transportes,
        'paginator': paginator
    }
    
    return render(request, "departamento/transporte.html", data)

class error_404(TemplateView):
    template_name = "departamento/404.html"