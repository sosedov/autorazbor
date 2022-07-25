from pickletools import markobject
from django.shortcuts import render

from cars.models import CarMark, CarModel, CarSubmodel
from parts.models import PartCategory, PartSubCategory, Parts
# Create your views here.
def authorization(request):
    return render(request, 'main/authorization.html')

def usercab(request):
    return render(request, 'main/usercab.html')

def search(request):
    filter = {}
    if request.GET.get('mark'):
        filter['car_submodel__car_model__car_mark__name'] = request.GET['mark']
    marks = CarMark.objects.all()
    models = CarModel.objects.all()
    submodels = CarSubmodel.objects.all()
    parts = []
    if filter:
        parts = Parts.objects.filter(**filter)
    return render(request, 'main/search.html', {
        'mark': marks,
        'model': models,
        'submodel': submodels,
        'parts': parts,
        })

def parts(request):
    parts = Parts.objects.all()
    data = dict(
        parts=parts,
    )
    return render(request, 'main/parts.html', data)
    
def order(request):
    return render(request, 'main/order.html')
