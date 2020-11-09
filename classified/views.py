from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def classified(request):
    
    return render(request, 'classified/classified.html')