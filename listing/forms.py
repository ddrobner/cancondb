from django.forms import ModelForm
from listing.models import Artist

class ArtistSubmission(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'link', 'notes', 'source', 'genres']