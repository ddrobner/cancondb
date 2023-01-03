from django.shortcuts import render
from django.http import HttpResponse
from taggit.models import Tag

from .forms import ArtistSubmission

# Create your views here.
def genres(request):
    tags = list(str(x) for x in Tag.objects.all())
    sorted_tags =  sorted(tags)
    return render(request, 'genres.html', {'tags': sorted_tags})

def submit(request):
    if request.method == 'POST':
        form = ArtistSubmission(request.POST)
        if form.is_valid():
            artist = form.save()
            return HttpResponse("Successful Submission")
    
    else:
        form = ArtistSubmission()
    
    return render(request, 'submission.html', {'form': form})

def listing(request):
    return HttpResponse("Placeholder")

        
