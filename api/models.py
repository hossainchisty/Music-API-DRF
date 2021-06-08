from django.db import models

class Singer(models.Model):
    artist = models.CharField(max_length=40)

    def __str__(self):
        return self.artist

class Song(models.Model):
    title = models.CharField(max_length=50) 
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE, related_name='song_by')
    duration = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.title}  Artist-{self.singer}"
