from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'vehiculo/index.html', {'title': 'Catálogo de Vehículos'})

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo agregado exitosamente.')
            return redirect('listar_vehiculos')  
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()

    bajo = vehiculos.filter(precio__lte=10000)
    medio = vehiculos.filter(precio__gt=10000, precio__lte=30000)
    alto = vehiculos.filter(precio__gt=30000)

    return render(request, 'vehiculo/listar_vehiculos.html', {
        'bajo': bajo,
        'medio': medio,
        'alto': alto,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, 'Registro exitoso! Has iniciado sesión.')
            return redirect('index')  
    else:
        form = UserCreationForm()
    return render(request, 'vehiculo/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión exitosamente.')
            return redirect("index") 
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, "vehiculo/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect("index")
