from django.db import models

class Orphanage(models.Model):

    def __unicode__(self):
        return self.name

    orid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    address = models.TextField(max_length=1000)
    contact_number = models.CharField(max_length=35)
    description = models.TextField(max_length=4000)
    no_of_images = models.IntegerField(default=0)
    donation_link = models.CharField(max_length=250)
    

class Oldagehome(models.Model):

    def __unicode__(self):
        return self.name

    olid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    address = models.TextField(max_length=1000)
    contact_number = models.CharField(max_length=35)
    description = models.TextField(max_length=4000)
    donation_link = models.CharField(max_length=250)
# Create your models here.
