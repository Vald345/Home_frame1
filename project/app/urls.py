from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('hello/',index,name='index'),
    path('pytho/',index2,name='index2'),
    path('homework/',index2,name='index3'),
]
