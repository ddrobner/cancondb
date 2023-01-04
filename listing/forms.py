from django.forms import ModelForm
from listing.models import Artist
from captcha.fields import ReCaptchaField

class ArtistSubmission(ModelForm):
    captcha = ReCaptchaField() 
    class Meta:
        model = Artist
        fields = ['name', 'link', 'notes', 'source', 'genres']

    def save(self, commit=True):
        return super(ArtistSubmission, self).save(commit=commit)