from django.shortcuts import redirect
from .forms import EmployeeForm
from django.shortcuts import render, get_object_or_404
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hr/employee_list.html', {'employees': employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr/employee_details.html', {'employee': employee})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hr/create_employee.html', {'form': form})


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('hr:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hr/update_employee.html', {'form': form})


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('hr:employee_list')
    return render(request, 'hr/delete_employee.html', {'employee': employee})
