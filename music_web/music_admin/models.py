from django.db import models

# Create your models here.


class Scale(models.Model):

    name = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    discription = models.TextField()
    scale_img = models.ImageField(upload_to='scales/', default="x")

    def __str__(self):
        return self.name