from django.shortcuts import render
from .models import Album

def home(request):
    albums = Album.objects
    return render(request, 'smallview/home.html', {'albums':albums})