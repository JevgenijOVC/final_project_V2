from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, ProductForOrder
from .forms import OrderForm, ProductForOrderForm
from django.http import Http404


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order/order_detail.html', {'order': order})


def create_order(request):
    if request.method == 'POST':
        form1 = OrderForm(request.POST)
        form2 = ProductForOrderForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('order:order_list')
    else:
        form1 = OrderForm()
        form2 = ProductForOrderForm()
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'order/create_order.html', context)


def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    product = ProductForOrder.objects.get(pk=pk)
    if request.method == 'POST':
        form1 = OrderForm(request.POST, instance=order)
        form2 = ProductForOrderForm(request.POST, instance=product)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('order:order_list')
    else:
        form1 = OrderForm(instance=order)
        form2 = ProductForOrderForm(instance=product)
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'order/update_order.html', context)


def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order:order_list')
    return render(request, 'order/delete_order.html', {'part': order})














