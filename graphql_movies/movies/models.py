from django.db import models

# Create your models here.

class MovieList(models.Model):
    title =models.CharField(max_length=100)
    vote_average = models.FloatField()
    overview =  models.TextField()
    release_date = models.CharField(max_length=100)




class CreateList(models.Model):

    list_name= models.CharField(max_length=100)
    movie_list=models.CharField(max_length=500)
    recommend_movie_list=models.CharField(max_length=500,default="")

    class Meta:
        ordering = ('list_name',)




