from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.
# def demo(request):
#   return HttpResponse("hello world")
def demo(request):
    obj = models.Place.objects.all()
    objj = models.Person.objects.all()
    return render(request, "index.html", {'result': obj,'result1': objj})
