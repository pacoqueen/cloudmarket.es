from django.db import models

# Create your models here.

class Item(models.Model):
    description = models.CharField(max_length = 256)
    url = models.URLField()
    notes = models.TextField()
    photo = models.ImageField(upload_to = "img")

    def __unicode__(self):
        return self.description


class Person(models.Model):
    nombre = models.CharField(max_length = 128)

    def __unicode__(self):
        return self.nombre


class Gift(models.Model):
    person = models.ForeignKey(Person)
    item = models.ForeignKey(Item)
    date = models.DateField()
    done = models.BooleanField()

    def __unicode__(self):
        return self.nombre

