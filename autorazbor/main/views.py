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
    marks = CarMark.objects.all()
    models = CarModel.objects.all()
    submodels = CarSubmodel.objects.all()
    parts = Parts.objects.all()
    return render(request, 'main/search.html', {
        'mark': marks,
        'model': models,
        'submodel': submodels,
        'parts': parts,
        })

def parts(request):
    return render(request, 'main/parts.html')
    
def order(request):
    return render(request, 'main/order.html')
