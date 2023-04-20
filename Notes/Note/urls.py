
from django.contrib import admin
from django.urls import path,include
from .views import*
from . import views

urlpatterns = [
    path('note/',views.Note,name='note'),
    path('insert/',views.insert,name="insert"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('read/<int:id>',views.read,name='read')
    
]
