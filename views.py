
# Create your views here.
# employees/views.py
from django.shortcuts import HttpResponse, get_object_or_404, render, redirect # type: ignore
from .models import Employee_data
from .forms import EmployeeForm


def home(request):
    return HttpResponse('Welcome to CRUD')

def employee_list(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print(Employee_data.objects.all())
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    employees = Employee_data.objects.all()
    return render(request, 'employee_list.html', {'form': form, 'employees': employees})

def employee_update(request, employee_id):
    employee = get_object_or_404(Employee_data, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
            
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {'form': form, 'employee': employee})

def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee_data, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_list.html', {'employees': Employee_data.objects.all()})