from django.shortcuts import render
from .models import Item

def video(request):
    
    return render(request, 'video.html')