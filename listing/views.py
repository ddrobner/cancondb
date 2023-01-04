from django.shortcuts import render
from django.http import HttpResponse
from taggit.models import Tag

from .forms import ArtistSubmission

# Create your views here.
def genres(request):
    tags = list(str(x) for x in Tag.objects.all())
    #slugs = list(x.slug() for x in Tag.objects.all())
    sorted_tags =  sorted(tags)
    sorted_slugs = sorted(Tag.objects.all().values_list("slug", flat=True))
    genre_data = zip(sorted_tags, sorted_slugs)

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

        
