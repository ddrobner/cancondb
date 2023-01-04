from django.forms import ModelForm
from listing.models import Artist

class ArtistSubmission(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'notes', 'source', 'genres']

        def save(self, ip, commit=True):
            instance = super(ArtistSubmission, self).save(commit=False)
            instance.user_ip = str(ip)
            if commit:
                instance.save
            return instance
