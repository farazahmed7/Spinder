from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Location
from django.contrib.auth.models import User
from math import cos, asin, sqrt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view


def distance(request):
    if request.method=="POST":
        p = 0.017453292519943295
        lat1=str(request.POST['latitude'])
       # lat2=38.897147
        lon1=str(request.POST['longitude'])
       # lon2=-77.043934
        list=[]
        for x in Location.objects.all():
            a = 0.5 - cos((float(x.latitude) - lat1) * p)/2 + cos(lat1 * p) * cos(float(x.latitude) * p) * (1 - cos((float(x.longitude) - lon1) * p)) / 2
            result=round(12742 * asin(sqrt(a)),2)
            list.append(x.user.first_name+str(result)+"  ")

        return HttpResponse(list)

    return HttpResponse(a)

@csrf_exempt
@api_view(['GET', 'POST', ])
def createUser(request):
    if request.method=="POST":
        _user=str(request.POST['user'])
        _email=str(request.POST['email'])
        _password=str(request.POST['password'])
        User.objects.create_user(_user,_email,_password)
        return HttpResponse("Registered")

    return HttpResponse("Error")

@csrf_exempt
@api_view(['GET', 'POST', ])
def loginUser(request):
     if request.method=="POST":
        _user=str(request.POST['user'])
        _password=str(request.POST['password'])
        user=authenticate(username=_user,password=_password)
        if user is not None:
            return HttpResponse(user.email)
        else:
            return HttpResponse("First signup please")

@api_view(['GET', 'POST', ])
def addLocation(request):
    if request.method=="POST":
        _email=str(request.POST['email'])
        lat1=str(request.POST['latitude'])
        lon1=str(request.POST['longitude'])
        user=User.objects.get(email=_email)

        Location.objects.update_or_create(user=user,longitude=lon1,latitude=lat1)
        return HttpResponse("Added")
    return HttpResponse("faraz")

