from pickle import GET

from django.http import HttpResponse
from django.shortcuts import render
from . models import place,person

# Create your views here.
def home(request):
    obj=place.objects.all()
    obj2=person.objects.all()
    return render(request,'index.html',{"result":obj,
    'x':obj2})



# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     div=x/y
#     mul=x*y
#     return render(request,'result.html',{'addition':add,
#                                          'subtraction':sub,
#                                          'division':div,
#                                          'multiplication':mul})
