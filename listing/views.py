from django.shortcuts import render
from django.http import HttpResponse
from taggit.models import Tag

from .forms import ArtistSubmission

# Create your views here.
def genres(request):
    tags = sorted(list(str(x) for x in Tag.objects.all().values_list("name", flat=True)), key=str.casefold)
    slugs = sorted(Tag.objects.all().values_list("slug", flat=True), key=str.casefold)
    genre_data = zip(tags, slugs)

    return render(request, 'genres.html', {'genre_data': genre_data})

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

def genre_view(request, genre_id):
    return HttpResponse(str(genre_id))

def artist_view(request, artist_id):
    return HttpResponse(str(artist_id))

        
