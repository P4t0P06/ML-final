from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PlantForm
from .models import Plant

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'plants': plants})

@login_required
def plants(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save()
            return redirect('plants')
    else:
        form = PlantForm()
    all_plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants.html', {'plants': all_plants, 'form': form})

@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')
