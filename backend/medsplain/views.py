from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# write a simple view that returns a string
def home(request):
    return HttpResponse("Starting the project medsplain.Lets go.")
