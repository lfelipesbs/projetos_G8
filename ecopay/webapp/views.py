from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore

def login(request):
        
    return render(request, 'front/login.html')
