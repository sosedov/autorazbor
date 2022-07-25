from http.client import REQUEST_URI_TOO_LONG
from django.shortcuts import render
from django.views import View

from .models import CarMark, CarModel, CarSubmodel

class Cars(View):
    def GetCarMark(request):
        mark = CarMark.objects.all()
        return render(request, 'main/search.html', {'mark': mark})

    def GetCarModel(request):
        model = CarModel.objects.all()
        return render(request, 'main/search.html', {'model': model})

    def GetCarSubmodel(request):
        submodel = CarSubmodel.objects.all()
        return render(request, 'main/search.html', {'submodel': submodel})