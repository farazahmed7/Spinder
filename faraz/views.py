from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Location
from django.contrib.auth.models import User
from math import cos, asin, sqrt


def distance(request):
    if request.method=="GET":
        p = 0.017453292519943295
        lat1=38.897147
       # lat2=38.897147
        lon1=-77.043934
       # lon2=-77.043934
        list=[]
        for x in Location.objects.all():
            a = 0.5 - cos((float(x.latitude) - lat1) * p)/2 + cos(lat1 * p) * cos(float(x.latitude) * p) * (1 - cos((float(x.longitude) - lon1) * p)) / 2
            result=round(12742 * asin(sqrt(a)),2)
            list.append(str(result)+" ")

        return HttpResponse(list)

    return HttpResponse(a)

def createUser(request):
    if request.method=="POST":
        _user=str(request.POST['user'])
        _email=str(request.POST['email'])
        _password=str(request.POST['password'])
        User.objects.create_user(_user,_email,_password)


