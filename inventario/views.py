from django.shortcuts import render
# inventario/views.py

from django.shortcuts import render, redirect
from .models import Material
from .forms import MaterialForm

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'inventario/material_list.html', {'materials': materials})

def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'inventario/material_form.html', {'form': form})

def material_update(request, pk):
    material = Material.objects.get(pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'inventario/material_form.html', {'form': form})

# Create your views here.
