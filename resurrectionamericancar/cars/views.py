import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Cars
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def cars_list(request):
    # return HttpResponse("listado")
    carros = Cars.objects.all()

  # Aplicar filtros según los parámetros del formulario
    marca = request.GET.get('marca')
    fuel_type = request.GET.get('fuel_type')
    year_min = request.GET.get('year_min') 
    year_max = request.GET.get('year_max')  
    precio_min = request.GET.get('precio_min') or 2000  # valor predeterminado
    precio_max = request.GET.get('precio_max') or 360000  # valor predeterminado
    color = request.GET.get('color')
    nuevo_usado = request.GET.get('nuevo_usado')
    only_oneowner = request.GET.get('only_oneowner')

    if marca:
        carros = carros.filter(marca=marca)
    if fuel_type:
        carros = carros.filter(fuel_type=fuel_type)
    if year_min:
        carros = carros.filter(year__gte=year_min)
    if year_max:
        carros = carros.filter(year__lte=year_max)
    carros = carros.filter(precio__gte=precio_min, precio__lte=precio_max)
    if color:
        carros = carros.filter(color=color)
    if nuevo_usado:
        carros = carros.filter(nuevo_usado=nuevo_usado)
    if only_oneowner == 'true':
        carros = carros.filter(only_oneowner=True)

    #paginador 
    paginator = Paginator(carros, 3)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)

    #fin paginador
    
    # current_year = datetime.datetime.now().year  # Año actual
    # year_range = list(range(2000, current_year + 1))  # Genera el rango de años

  
    
    #Pasar el año actual al contexto
    # context = {
    #     'cars': cars,
    #     #'current_year': current_year,
    #     #'year_range': year_range,  # Pasa la lista de años al contexto
    # }
    
    return render(request, 'cars/cars_list.html', {'cars': cars})
    # return render(request, 'cars/cars_list.html', context)

def car_page(request,id):
    # return HttpResponse(slug)
    car = get_object_or_404(Cars, id=id)
    return render(request,'cars/cars_page.html',{'car':car})

@login_required(login_url="users:login")
def car_new(request):
    if request.method == 'POST':
        form = forms.CrearCar(request.POST, request.FILES)
        if form.is_valid():
            newcar = form.save(commit=False)
            newcar.usuario = request.user
            newcar.save()
            return redirect('cars:list')       
    else:
        form = forms.CrearCar()
    return render(request, 'cars/car_new.html', {'form': form})

