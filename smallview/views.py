from django.shortcuts import render, get_object_or_404
from .models import Album

def home(request):
    
    first  = get_object_or_404(Album, feature_key=1)
    second = get_object_or_404(Album, feature_key=2)
    third  = get_object_or_404(Album, feature_key=3)
    fourth = get_object_or_404(Album, feature_key=4)
    fifth  = get_object_or_404(Album, feature_key=5)
    sixth  = get_object_or_404(Album, feature_key=6)
    # sixth   = Album.objects.filter(feature_key=6)
    
    return render(request, 'smallview/home.html', {
       'first':first,
       'second':second,
       'third':third,
       'fourth':fourth,
       'fifth':fifth,
       'sixth':sixth
        })