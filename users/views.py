from django.core import paginator
from django.shortcuts import render, redirect
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse, response
from django.contrib import messages
from django.views.generic.base import TemplateView
from .forms import UCFWithEmail, AFWithEmail, ContactoForm, ArriendoForm, PasajeroForm, PagoForm
from django.core.paginator import Paginator
from django.http import Http404
from departamento.models import Departamento, Servicio, Zona , Transporte, Arriendo,  Tiposervicio, Pasajero
from django.db.models import Q
from django.forms import formset_factory
from django.views.generic.edit import FormView
from departamento.filters import ServicioFilter, TransporteFilter

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
    departamentos = Departamento.objects.all()

    data = {
        'departamentos': departamentos

    }

    return render(request, "departamento/principal.html", data)

def index(request):
    return render(request, "departamento/index.html")

def cuenta(request):
    return render(request, "departamento/cuenta.html")

def contacto(request):
    zonas = Zona.objects.all()


    data = {
        'zonas': zonas,
        'form':ContactoForm()
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Contacto Guardado')
        else:
            data["form"] = formulario


    return render(request, "departamento/contacto.html", data)

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
        'paginator': paginator,

    }

    return render(request, "departamento/dptos.html", data)

def listadoServicios(request):
    busqueda = request.GET.get("buscarServicio")
    servicios = Servicio.objects.all()
    tiposervicio = Tiposervicio.objects.all()
    zonas = Zona.objects.all()
    departamentos = Departamento.objects.all()
    miFiltro = ServicioFilter(request.GET, queryset=servicios)
    servicios = miFiltro.qs


    page = request.GET.get('page', 1)

    if busqueda:
        servicios = Servicio.objects.filter(
            Q(precio__icontains = busqueda) |
            Q(zona__nombre__icontains = busqueda) |
            Q(departamento__nombre__icontains = busqueda) |
            Q(tipo__tipo__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(servicios, 9)
        servicios = paginator.page(page)
    except:
        raise response.Http404

    data = {
        'entity': servicios,
        'paginator': paginator,
        'tiposervicio':tiposervicio,
        'zonas':zonas,
        'departamentos':departamentos,
        'miFiltro': miFiltro,
    }

    return render(request, "departamento/listadoServicios.html", data)

def arrendar(request, pk):
    zonas = Zona.objects.all()
    departamentos = Departamento.objects.get(id=pk)
    dptos = Departamento.objects.all()

    data = {
        'zonas': zonas,
        'departamentos': departamentos,
        'dptos': dptos,
        'form': ArriendoForm()

    }

    if request.method == "POST":
        formulario = ArriendoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Ahora por favor, ingrese los siguientes datos')
            return redirect('/pasajero')
        else:
            data["form"] = formulario

    return render(request, "departamento/arrendar.html", data)

def pago(request):
    arriendo = Arriendo.objects.last()
    departamento = Departamento.objects.get(nombre=arriendo.departamento)

    data = {
        'arriendo': arriendo,
        'departamento':departamento,
        'form':PagoForm()

    }

    if request.method == "POST":
        formulario = PagoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Ahora si desea puede contratar un servicio extra')
            return redirect('/datosArriendo') 
        else:
            data["form"] = formulario

    return render(request, "departamento/pago.html", data)

def servicios(request):

    return render(request, "departamento/servicios.html")

def transporte(request):
    busqueda = request.GET.get("buscarTransporte")
    transportes = Transporte.objects.all()
    zonas = Zona.objects.all()
    departamentos = Departamento.objects.all()

    miFiltro = TransporteFilter(request.GET, queryset=transportes)
    transportes = miFiltro.qs

    page = request.GET.get('page', 1)

    if busqueda:
        transportes = Transporte.objects.filter(
            Q(nombreConductor__icontains = busqueda) |
            Q(departamento__nombre__icontains = busqueda) |
            Q(zona__nombre__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(transportes, 9)
        transportes = paginator.page(page)
    except:
        raise response.Http404

    data = {
        'entity': transportes,
        'zonas':zonas,
        'departamentos':departamentos,
        'miFiltro':miFiltro,
        'paginator': paginator
    }
    
    return render(request, "departamento/transporte.html", data)

class pasajero(FormView):
    template_name = 'departamento/acompañantes.html'
    arriendo = Arriendo.objects.all().last()
    form_class = formset_factory(PasajeroForm, extra=1)
    
    def form_valid(self, form):

        for f in form:
            f.save()
        
        return redirect('/pago')

        return super(pasajero, self).form_valid(form)

def contratoServicio(request, pk):
    servicios = Servicio.objects.get(id=pk)

    data = {
        'servicios': servicios,
    }
    return render(request, "departamento/contratoServicio.html", data)

def contratoTransporte(request, pk):
    transportes = Transporte.objects.get(id=pk)

    data = {
        'transportes': transportes,
    }

    return render(request, "departamento/contratoTransporte.html", data)

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('departamento/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('departamento/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

def datosArriendo(request):
    arriendo = Arriendo.objects.last()
    data = {
        'arriendo': arriendo,
    }

    return render(request, "departamento/datosArriendo.html", data)

class error_404(TemplateView):
    template_name = "departamento/404.html"