from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Artist(models.Model):
    # storing some basic info about the artist in the DB
    name = models.CharField(max_length=50, verbose_name="Artist Name")
    # link to the artist
    link = models.URLField(verbose_name="URL To Artist")
    # notes in case it's relevant
    notes = models.CharField(max_length=150, blank=True, verbose_name="Notes")
    # source that the artist is canadian
    # considering making this optional
    source = models.URLField(verbose_name="Source That The Artist Is Canadian", blank=True)
    # storing genre tags
    genres = TaggableManager(verbose_name = "Genres", help_text="A comma separated list of genres")
    # artist slug
    slug = models.SlugField(unique=True)
    # IP of user who submitted the artist
    user_ip = models.GenericIPAddressField(default="0.0.0.0")

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        instance.slug = slugify(instance.name)
    
    # toString method
    def __str__(self):
        return self.name

pre_save.connect(Artist.pre_save, Artist)