from django.shortcuts import render,redirect,get_list_or_404
from .models import add
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.

def Note(request):
    data=add.objects.all()
   
    

    return render(request,'new.html',{'content':data})

def insert(request):
    
    if request.method=='POST':
        form=NewNote(request.POST)
        if(form.is_valid()):
            form.save()
            return Note(request)
    else:
        form=NewNote()
    
    return render(request,'insert.html')

def update(request,id):
    
    form=NewNote()
    if(request.method=='POST'):
        obj=add.objects.get(id=id)
        print(request.POST)
        form=NewNote(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
       
        return Note(request)

    return render(request,'update.html',{'form':form})
def delete(request,id):
    element=add.objects.get(id=id)
    element.delete()
    return Note(request)

def read(request,id):
    element=add.objects.get(id=id)
    
    return render(request,"read.html",{"info":element})

