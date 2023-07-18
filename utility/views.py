from django.shortcuts import render, get_object_or_404, redirect
from .models import Unit, ComponentType
from .forms import UnitFrom, ComponentTypeFrom


def under_construction(request):
    return render(request, 'utility/under_construction.html')


def utility(request):
    return render(request, 'utility/utility.html')


# UNIT CRUD ---------------------------
def unit_list(request):
    units = Unit.objects.all()
    return render(request, 'utility/unit/unit_list.html', {'units': units})


def create_unit(request):
    if request.method == 'POST':
        form = UnitFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utility:unit_list')
    else:
        form = UnitFrom()
    return render(request, 'utility/create.html', {'form': form})


def update_unit(request, pk):
    unit = Unit.objects.get(pk=pk)
    if request.method == 'POST':
        form = UnitFrom(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('utility:unit_list')
    else:
        form = UnitFrom(instance=unit)
    return render(request, 'utility/update.html', {'form': form})


def delete_unit(request, pk):
    unit = Unit.objects.get(pk=pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('production:part_list')
    return render(request, 'utility/delete.html', {'unit': unit})


# COMPONENT TYPE CRUD ---------------------------
def component_type_list(request):
    component_type = ComponentType.objects.all()
    return render(request, 'utility/component_type/component_type_list.html', {'component_type': component_type})


def create_component_type(request):
    if request.method == 'POST':
        form = ComponentTypeFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utility:component_type_list')
    else:
        form = ComponentTypeFrom()
    return render(request, 'utility/create.html', {'form': form})


def update_component_type(request, pk):
    component_type = ComponentType.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComponentTypeFrom(request.POST, instance=component_type)
        if form.is_valid():
            form.save()
            return redirect('utility:component_type_list')
    else:
        form = ComponentTypeFrom(instance=component_type)
    return render(request, 'utility/update.html', {'form': form})


def delete_component_type(request, pk):
    component_type = ComponentType.objects.get(pk=pk)
    if request.method == 'POST':
        component_type.delete()
        return redirect('utility:component_type_list')
    return render(request, 'utility/delete.html', {'component_type': component_type})

