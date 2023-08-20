from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Player(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    utr = models.FloatField(default=0.00)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name