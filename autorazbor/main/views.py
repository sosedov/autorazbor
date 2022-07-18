from django.shortcuts import render

# Create your views here.
def authorization(request):
    return render(request, 'main/authorization.html')

def usercab(request):
    return render(request, 'main/usercab.html')

def search(request):
    return render(request, 'main/search.html')

def parts(request):
    return render(request, 'main/parts.html')
    
def order(request):
    return render(request, 'main/order.html')