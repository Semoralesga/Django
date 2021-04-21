from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from .models import Registration

# Create your views here.

def homePageView(request):
    return HttpResponse("<h2>Hola mundo!</h2>")

def aboutPageView(request):
    return HttpResponse("<h2>About us!</h2>")

class RegistrationCreate(CreateView):
    model =Registration
    fields = ['fname','lname','city','email']