from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, UpdateEmployeeForm, SearchForm
from .models import Employee


# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request, "emp_list.html", {"employees": employees})


def add_emp(request):
    if request.method == "POST":
        add_emp_form = EmployeeForm(request.POST)
        if add_emp_form.is_valid():
            add_emp_form.save()
            return redirect("home")
    else:
        add_emp_form = EmployeeForm()
    return render(request, "add_emp.html", {"form": add_emp_form})


def update_emp(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        if request.method == "POST":
            update_emp_form = UpdateEmployeeForm(request.POST, instance=employee)
            if update_emp_form.is_valid():
                update_emp_form.save()
                return redirect("home")
        else:
            update_emp_form = UpdateEmployeeForm(instance=employee)
        return render(request, "update_emp.html", {"form": update_emp_form})

    except Employee.DoesNotExist:
        message = """
        <div style="text-align: center;">
            <h1>Employee doesn't exist!</h1>
            <h2><a href="/action/">Go to Homepage</a></h2>
        </div>
        """
        return HttpResponse(message)


def delete_emp(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return redirect("action")
    except Employee.DoesNotExist:
        message = """
        <div style="text-align: center;">
            <h1>Employee doesn't exist!</h1>
            <h2><a href="/action/">Go to Homepage</a></h2>
        </div>
        """
        return HttpResponse(message)


def emp_details(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        return render(request, "emp_details.html", {"employee": employee})
    except Employee.DoesNotExist:
        message = """
        <div style="text-align: center;">
            <h1>Employee doesn't exist!</h1>
            <h2><a href="/">Go to Homepage</a></h2>
        </div>
        """
        return HttpResponse(message)


def action(request):
    employees = Employee.objects.all()

    if request.method == "POST":
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            query = search_form.cleaned_data.get("query")

        if query != "":
            employees = [
                employee
                for employee in employees
                if query.lower() in employee.name.lower()
            ]
            return render(
                request,
                "action.html",
                {"employees": employees, "search_form": search_form},
            )

    employees = []
    search_form = SearchForm()

    return render(
        request, "action.html", {"employees": employees, "search_form": search_form}
    )
