from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, Customer
from .forms import SupplierForm, CustomerForm


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'crm/suppliers/suppliers_list.html', {'suppliers': suppliers})


def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'crm/suppliers/supplier_detail.html', {'supplier': supplier})


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'crm/standard_create.html', {'form': form})


def update_supplier(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('crm:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'crm/standard_update.html', {'form': form})


def delete_supplier(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('crm:supplier_list')
    return render(request, 'crm/standard_delete.html', {'supplier': supplier})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customers/customers_list.html', {'customers': customers})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'crm/customers/customer_detail.html', {'customer': customer})


def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'crm/standard_create.html', {'form': form})


def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('crm:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'crm/standard_update.html', {'form': form})


def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('crm:customer_list')
    return render(request, 'crm/standard_delete.html', {'customer': customer})
