from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hello Django")
def room(request):
    return HttpResponse("welcome to the room")