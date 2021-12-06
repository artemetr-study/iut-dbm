from datetime import datetime

from django.shortcuts import render, redirect

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from lab_5.models import Crew, Position, Employee
from django.views.decorators.csrf import csrf_exempt


def crews(request):
    return render(request, 'model_list.html', {'name': 'crew', 'models': Crew.objects.all()})


@csrf_exempt
def add_crew(request):
    if request.method == 'POST':
        model = Crew()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/crews/')
    else:
        return render(request, 'model_add.html', {'type': 'crew'})


@csrf_exempt
def edit_crew(request, id: int):
    if request.method == 'POST':
        model = Crew.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/crews/')
    else:
        return render(request, 'model_edit.html', {'type': 'crew', 'model': Crew.objects.get(id=id)})


@csrf_exempt
def delete_crew(request, id: int):
    model = Crew.objects.get(id=id)
    model.delete()
    return redirect('/crews/')


def positions(request):
    return render(request, 'model_list.html', {'name': 'position', 'models': Position.objects.all()})


@csrf_exempt
def add_position(request):
    if request.method == 'POST':
        model = Position()
        model.name = request.POST.get('name')
        model.save()
        return redirect('/positions/')
    else:
        return render(request, 'model_add.html', {'type': 'position'})


@csrf_exempt
def edit_position(request, id: int):
    if request.method == 'POST':
        model = Position.objects.get(id=id)
        model.name = request.POST.get('name')
        model.save()
        return redirect('/positions/')
    else:
        return render(request, 'model_edit.html', {'type': 'position', 'model': Position.objects.get(id=id)})


@csrf_exempt
def delete_position(request, id: int):
    model = Position.objects.get(id=id)
    model.delete()
    return redirect('/positions/')


def employees(request):
    return render(request, 'model_list.html', {'name': 'employee', 'models': Employee.objects.all()})


@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        model = Employee()
        model.lastname = request.POST.get('lastname')
        model.firstname = request.POST.get('firstname')
        model.middlename = request.POST.get('middlename')
        model.birthday = datetime.fromisoformat(request.POST.get('birthday')) if request.POST.get('birthday') else datetime.fromisoformat('1970-01-01')
        model.hiring_date = datetime.fromisoformat(request.POST.get('hiring_date')) if request.POST.get('hiring_date') else None
        model.dismissal_date = datetime.fromisoformat(request.POST.get('dismissal_date')) if request.POST.get('dismissal_date') else None
        model.salary = float(request.POST.get('salary'))
        model.position_id = int(request.POST.get('position_id')) or None
        model.crew_id = int(request.POST.get('crew_id')) or None
        model.save()
        return redirect('/employees/')
    else:
        return render(request, 'employee_add.html', {'type': 'employee', 'positions': Position.objects.all(), 'crews': Crew.objects.all()})


@csrf_exempt
def edit_employee(request, id: int):
    if request.method == 'POST':
        model = Employee.objects.get(id=id)
        model.lastname = request.POST.get('lastname')
        model.firstname = request.POST.get('firstname')
        model.middlename = request.POST.get('middlename')
        model.birthday = datetime.fromisoformat(request.POST.get('birthday')) if request.POST.get(
            'birthday') else datetime.fromisoformat('1971-01-01')
        print(datetime.fromisoformat('1970-01-01 00:00:00'))
        model.hiring_date = datetime.fromisoformat(request.POST.get('hiring_date')) if request.POST.get(
            'hiring_date') else None
        model.dismissal_date = datetime.fromisoformat(request.POST.get('dismissal_date')) if request.POST.get(
            'dismissal_date') else None
        model.salary = float(request.POST.get('salary'))
        model.position_id = int(request.POST.get('position_id')) or None
        model.crew_id = int(request.POST.get('crew_id')) or None
        model.save()
        return redirect('/employees/')
    else:
        return render(request, 'employee_edit.html', {'type': 'employee', 'model': Employee.objects.get(id=id), 'positions': Position.objects.all(), 'crews': Crew.objects.all()})


@csrf_exempt
def delete_employee(request, id: int):
    model = Employee.objects.get(id=id)
    model.delete()
    return redirect('/employees/')
