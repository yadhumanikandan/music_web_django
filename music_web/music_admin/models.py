from django.db import models

# Create your models here.


class Scale(models.Model):

    name = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    discription = models.TextField()
    keyboard_image = models.ImageField(upload_to='scales/keyboard', default="x")
    guitar_image = models.ImageField(upload_to='scales/guitar', default="x")

    def __str__(self):
        return self.name
    

class Chord(models.Model):

    name = models.CharField(max_length=100)
    chord = models.CharField(max_length=100)
    discription = models.TextField()
    keyboard_image = models.ImageField(upload_to='scales/keyboard', default="x")
    guitar_image = models.ImageField(upload_to='scales/guitar', default="x")

    def __str__(self):
        return self.name
    