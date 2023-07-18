from django.shortcuts import render, get_object_or_404, redirect
from .models import Component, Part, Operation, OperationsForPart
from .forms import PartForm, ComponentForm, OperationForm, OperationsForPartForm
from django.http import Http404


def part_list(request):
    parts = Part.objects.all()
    return render(request, 'production/part/part_list.html', {'parts': parts})


def part_detail(request, pk):
    part = get_object_or_404(Part, pk=pk)
    return render(request, 'production/part/part_details.html', {'part': part})


def create_part(request):
    if request.method == 'POST':
        form1 = PartForm(request.POST)
        form2 = OperationsForPartForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('production:part_list')
    else:
        form1 = PartForm()
        form2 = OperationsForPartForm()
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'production/part/create_part.html', context)


def update_part(request, pk):
    part = Part.objects.get(pk=pk)
    operation = OperationsForPart.objects.get(pk=pk)
    if request.method == 'POST':
        form1 = PartForm(request.POST, instance=part)
        form2 = OperationsForPartForm(request.POST, instance=operation)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('production:part_list')
    else:
        form1 = PartForm(instance=part)
        form2 = OperationsForPartForm(instance=operation)
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'production/part/update_part.html', context)


def delete_part(request, pk):
    part = Part.objects.get(pk=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('production:part_list')
    return render(request, 'production/standard_delete.html', {'part': part})


def component_list(request):
    components = Component.objects.all()
    return render(request, 'production/component/component_list.html', {'components': components})


def operation_list(request):
    operations = Operation.objects.all()
    return render(request, 'production/operation/operation_list.html', {'operations': operations})


def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    return render(request, 'production/component/component_detail.html', {'component': component})


def operation_detail(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    return render(request, 'production/operation/operation_detail.html', {'operation': operation})


def create_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('production:create_component')
    else:
        form = ComponentForm()
    return render(request, 'production/standard_create.html', {'form': form})


def create_operation(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('production:create_operation')
    else:
        form = OperationForm
    return render(request, 'production/standard_create.html', {'form': form})


def update_component(request, pk):
    component = Component.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('production:component_list')
    else:
        form = ComponentForm(instance=component)
    return render(request, 'production/standard_update.html', {'form': form})


def update_operation(request, pk):
    operation = Operation.objects.get(pk=pk)
    if request.method == 'POST':
        form = OperationForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            return redirect('production:operation_list')
    else:
        form = OperationForm(instance=operation)
    return render(request, 'production/standard_update.html', {'form': form})


def delete_component(request, pk):
    component = Component.objects.get(pk=pk)
    if request.method == 'POST':
        component.delete()
        return redirect('production:component_list')
    return render(request, 'production/standard_delete.html', {'component': component})


def delete_operation(request, pk):
    operation = Operation.objects.get(pk=pk)
    if request.method == 'POST':
        operation.delete()
        return redirect('production:operation_list')
    return render(request, 'production/standard_delete.html', {'operation': operation})
