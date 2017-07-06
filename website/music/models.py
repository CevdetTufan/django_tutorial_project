from django.db import models

# Create your models here.

class Albume(models.Model):
    artist=models.CharField(max_length=250)
    albume_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    albume_logo=models.CharField(max_length=1000)

    def __str__(self):
        return self.artist +" - "+self.albume_title


class Song(models.Model):
    albume=models.ForeignKey(Albume,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)

