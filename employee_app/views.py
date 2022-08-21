from django.shortcuts import render, HttpResponse
from .models import *
from datetime import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emp=Employee.objects.all()
    context={
        'emp': emp
    }
    return render(request, 'view_emp.html', context)


def add_emp(request):
    if request.method == "POST":
        firname=request.POST['f_name']
        lname=request.POST['lname']
        phone=request.POST['phone']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        dept=request.POST['dept']
        role=request.POST['role']

        new_employee=Employee(first_name=firname, last_name=lname, dept_id=dept,role_id=role ,salary=salary, bonus=bonus, phone=phone, hire_date=datetime.now())
        new_employee.save()
        return HttpResponse("<h1>Employee Added Successfully !!!</h1>")
    elif request.method == "GET":
        dept=Department.objects.all()
        role_obj=Role.objects.all()
        context={
            'dept': dept,
            'role_obj': role_obj
        }
        return render(request, 'add_emp.html', context)
    else:
        return HttpResponse("<h1>An Exception Occoured</h1>")

def remove_emp(request, id=0):
    if id:
        try:
            emp=Employee.objects.get(id=id)
            emp.delete()
            return HttpResponse("<h1>Employee Removed Successfully !!!</h1>")
        except:
            return HttpResponse("<h1>Enter a valid id</h1>")
    emp=Employee.objects.all()
    context={
        'emp': emp
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == "GET":
        emp=Employee.objects.all()
        context={
            'emp':emp
        }
        return render(request, 'choose_to_edit.html', context)
    # return render(request, 'filter_emp.html')

def send_emp_to_edit(request, id):
    if id:
        try:
            emp=Employee.objects.get(id=id)
            role_obj=Role.objects.all()
            dept=Department.objects.all()
            context={
                'emp': emp,
                'dept': dept,
                'role_obj': role_obj
            }
            return render(request, 'filter_emp.html', context)
        except:
            return HttpResponse("<h1>Choose A Valid Employee</h1>")

def handle_emp(request):
    if request.method == "POST":
        emp_id=request.POST['emp_id']
        emp=Employee.objects.get(id=emp_id)
        firname=request.POST['f_name']
        lname=request.POST['lname']
        phone=request.POST['phone']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])

        emp.first_name=firname
        emp.last_name=lname
        emp.phone=phone
        emp.salary=salary
        emp.bonus=bonus
        emp.save()

        return HttpResponse("<h1> Changes Saved Successfully !!! </h1>")
    else:
        return HttpResponse("<h1>Invalid Request $$$</h1>")