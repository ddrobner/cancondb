from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Artist(models.Model):
    # storing some basic info about the artist in the DB
    name = models.CharField(max_length=50)
    # notes in case it's relevant
    notes = models.CharField(max_length=150, blank=True)
    # source that the artist is canadian
    # considering making this optional
    source = models.URLField()
    # field for who submitted the artist
    # not publically viewable however want to prevent abuse
    submitted_by = models.EmailField(blank=False)
    # storing genre tags
    genres = TaggableManager()
    # artist slug
    slug = models.SlugField(slugify(name))

    # toString method
    def __str__(self):
        return self.name