from django.shortcuts import render
from .models import * 


def home(request):
    return render(request,'accueil.html')

def all_chef(request):
    all_chef=Chef.objects.all()
    return render(request,'chef.html',{'all_chefs':all_chef})

def detail_chef(request,id):
    detail_chef=Chef.objects.get(id=id)
    return render(request,'detail_chef.html',{'detail_chef':detail_chef})

def all_civilisation(request):
    all_civilisation=Civilisation.objects.all()
    return render(request,'civilisation.html',{'all_civilisation':all_civilisation}) 

def detail_civilisation(request,id):
    detail_civilisation=Civilisation.objects.get(id=id)
    return render(request,'detail_civilisation.html',{'detail_civilisation':detail_civilisation})


