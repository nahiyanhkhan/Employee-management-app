from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm


# Create your views here.
def home(request):
    return render(request, "emp_list.html")


def add_emp(request):
    if request.method == "POST":
        add_emp_form = EmployeeForm(request.POST)
        if add_emp_form.is_valid():
            add_emp_form.save()
            return redirect("home")
        else:
            add_emp_form = EmployeeForm(add_emp_form.errors)
    else:
        add_emp_form = EmployeeForm()
    return render(request, "add_emp.html", {"form": add_emp_form})
