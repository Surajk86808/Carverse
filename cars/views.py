from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    search_fields = Car.objects.values('model','year','state','color','body_style').distinct()
    data = {
        'cars': paged_cars,
        'search_fields': search_fields,
    }
    return render(request, 'cars/cars.html',data) 

def car_detail(request, id):
    single_car = get_object_or_404(Car,pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html',data)    


def search(request):
    cars = Car.objects.order_by('created_date')
    
    search_fields = Car.objects.values('model','year','state','color','body_style').distinct()
    data = {
        'search_fields': search_fields,
    }
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_title__icontains=keyword)
    
    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            color = cars.filter(color__iexact=color) 
            
    if 'model' in request.GET:
        model = request.GET['color']
        if model:
            model = cars.filter(model__iexact=model)  
            
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
           state = cars.filter(state__iexact=state)   
            
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            year = cars.filter(year__iexact=year)  
            
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            body_style = cars.filter(body_style__iexact=body_style)                                         
            
    data = {
        'cars': cars,
    }
     # Keywords
    return render(request,'cars/search.html',data)           