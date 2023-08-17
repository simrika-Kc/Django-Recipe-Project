from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    people=[
        {'name':'Roman','age':'20'},
        {'name':'roman','age':'30'},
        {'name':'RoMan','age':'10'},
        {'name':'rOMAn','age':'18'}  
    ]
    return render(request,"index.html",context={'people':people})
