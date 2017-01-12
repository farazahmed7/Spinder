__author__ = 'abc'

from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^location$', views.distance, name='distance'),
    url(r'^signUp$', views.createUser, name='createUser')

]