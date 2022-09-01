import email
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse
#from Portfolio.home.models import Contact
#from home.models import Contact

def home(request):
    #return HttpResponse("<html> <head>This is my homepage (/)</head></html>")
    #context = {'name': "Shruti", 'Course': "Django"}
    return render(request, 'home.html', context)
# Create your views here.

