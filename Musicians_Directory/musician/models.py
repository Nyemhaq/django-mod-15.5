from django.db import models

class Musician(models.Model):
    First_name = models.CharField(max_length = 50)
    Last_name = models.CharField(max_length = 50)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Instrument = models.TextField()
    
    def __str__(self):
            return self.First_name
    
