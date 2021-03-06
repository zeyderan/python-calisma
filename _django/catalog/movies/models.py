from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    def get_movie_image_path(self):
        return '/img/'+self.image