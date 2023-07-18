from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import ProductForm, OperationsForProductForm, ComponentsForProductForm, PartsForProductForm
from inventory.models import Product, PartsForProduct, ComponentsForProduct, OperationsForProduct


def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/products_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})


def create_product(request):
    if request.method == 'POST':
        form1 = ProductForm(request.POST)
        form2 = PartsForProductForm(request.POST)
        form3 = ComponentsForProductForm(request.POST)
        form4 = OperationsForProductForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            return redirect('inventory/products_list.html')
    else:
        form1 = ProductForm()
        form2 = PartsForProductForm()
        form3 = ComponentsForProductForm()
        form4 = OperationsForProductForm()
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    }
    return render(request, 'inventory/create_product.html', context)


def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    part = PartsForProduct.objects.get(pk=pk)
    component = ComponentsForProduct.objects.get(pk=pk)
    operation = OperationsForProduct.objects.get(pk=pk)
    if request.method == 'POST':
        form1 = ProductForm(request.POST, instance=product)
        form2 = PartsForProductForm(request.POST, instance=part)
        form3 = ComponentsForProductForm(request.POST, instance=component)
        form4 = OperationsForProductForm(request.POST, instance=operation)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            return redirect('inventory:product_list')
    else:
        form1 = ProductForm(instance=product)
        form2 = PartsForProductForm(instance=part)
        form3 = ComponentsForProductForm(instance=component)
        form4 = OperationsForProductForm(instance=operation)
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    }
    return render(request, 'inventory/update_product.html', context)


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('inventory:product_list')
    return render(request, 'utility/standard_delete.html', {'product': product})
