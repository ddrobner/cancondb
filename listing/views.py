from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from taggit.models import Tag

from .forms import ArtistSubmission
from .models import Artist

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
            # TODO redirect to new artist page
            return HttpResponseRedirect("/")
    
    else:
        form = ArtistSubmission()
    
    return render(request, 'submission.html', {'form': form})

def listing(request):
    return HttpResponse("Placeholder")

def genre_view(request, genre_id):
    tags = Tag.objects.filter(slug=genre_id).values_list('slug', flat='True')
    artists = Artist.objects.filter(genres__slug__in=tags)
    names = []
    slugs = []
    for a in artists:
        names.append(a.name)
        slugs.append(a.slug)
    print(names)
    print(slugs)

    artist_info = zip(names, slugs)

    return render(request, 'genreView.html', {"artists": artist_info})

def artist_view(request, artist_id):
    return HttpResponse(str(artist_id))

        
