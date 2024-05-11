from django.db import models

# Create your models here.
class USER(models.Model):
    username=models.CharField(max_length=500)
    recipename=models.CharField(max_length=500)
    dietlabel=models.CharField(max_length=500)
    cuisine=models.CharField(max_length=500)
    dish=models.CharField(max_length=500)
    ingredients=models.CharField(max_length=500)
    health=models.CharField(max_length=500)
    image=models.FileField(upload_to="RECIPE_APP/images/")

    def __str__(self):
        return self.username
