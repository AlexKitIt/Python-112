from django.db import models


class Dog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='dog/images/')

    def __str__(self):
        return self.title
