from django.db import models
from musician.models import Musician

class Album(models.Model):
    Album_name = models.CharField(max_length = 100)
    Musician = models.ForeignKey(Musician , on_delete = models.CASCADE)
    Album_release_date = models.DateTimeField()
    Rating = models.IntegerField()
    
    def __str__(self):
            return self.Album_name