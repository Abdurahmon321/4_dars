from django.db import models

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=55)
    area = models.IntegerField()
    img = models.ImageField(upload_to="card_imgs/")
    population = models.BigIntegerField()

    def __str__(self):
        return self.name
