from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
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
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_ip = x_forwarded_for.split(',')[0]
        else:
            user_ip = request.META.get('REMOTE_ADDR')
        if form.is_valid():
            artist = form.save()
            artist.user_ip = str(user_ip)
            artist.save()
            # TODO redirect to new artist page
            return HttpResponseRedirect("/")
    
    else:
        form = ArtistSubmission()
    
    return render(request, 'submission.html', {'form': form})

def artist_listing(request):
    artists = Artist.objects.all()
    names = sorted(artists.values_list("name", flat="True"), key=str.casefold)
    slugs = sorted(artists.values_list("slug", flat=True), key=str.casefold)

    artist_data = zip(names, slugs)

    return render(request, 'artistListing.html', {"artist_data": artist_data})

def artist_view(request, artist_id):

    artist = model_to_dict(Artist.objects.get(slug=artist_id))
    print(artist)
    artist_name = artist["name"]
    artist.pop("name")
    artist_attributes = [a for a in artist.keys()]
    artist_values = [v for v in artist.values()]

    artist = zip(artist_attributes, artist_values)

    return render(request, "artistView.html", {"artist_name": artist_name, "artist": artist})
    

def genre_view(request, genre_id):
    tag = Tag.objects.get(slug=genre_id)
    artists = Artist.objects.filter(genres__slug=tag.slug)
    names = []
    slugs = []
    for a in artists:
        names.append(a.name)
        slugs.append(a.slug)

    artist_info = zip(names, slugs)

    return render(request, 'genreView.html', {"artists": artist_info, "genre_name" : tag.name})


        
