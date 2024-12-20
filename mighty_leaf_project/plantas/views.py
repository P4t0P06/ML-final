
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Planta
from .forms import PlantaForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_plantas')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def listar_plantas(request):
    plantas = Planta.objects.filter(usuario=request.user)
    return render(request, 'plantas/listar.html', {'plantas': plantas})

def create_planta(request):
    if request.method == 'POST':
        form = PlantaForm(request.POST)
        if form.is_valid():
            planta = form.save(commit=False)
            planta.usuario = request.user
            planta.save()
            return redirect('listar_plantas')
    else:
        form = PlantaForm()
    return render(request, 'plantas/create.html', {'form': form})

def edit_planta(request, id):
    planta = Planta.objects.get(id=id)
    if request.method == 'POST':
        form = PlantaForm(request.POST, instance=planta)
        if form.is_valid():
            form.save()
            return redirect('listar_plantas')
    else:
        form = PlantaForm(instance=planta)
    return render(request, 'plantas/edit.html', {'form': form})

def delete_planta(request, id):
    planta = Planta.objects.get(id=id)
    planta.delete()
    return redirect('listar_plantas')
