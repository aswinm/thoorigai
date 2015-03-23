from django.db import models

class Orphanage(models.Model):

    def __unicode__(self):
        return self.name

    orid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    address = models.TextField(max_length=1000)
    contact_number = models.CharField(max_length=35)
    description = models.TextField(max_length=5000)
    no_of_images = models.IntegerField(default=0)
    donation_link = models.CharField(max_length=250,blank=True,null=True)
    

class Oldagehome(models.Model):

    def __unicode__(self):
        return self.name

    olid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    address = models.TextField(max_length=1000)
    contact_number = models.CharField(max_length=35)
    description = models.TextField(max_length=5000)
    donation_link = models.CharField(max_length=250,blank=True,null=True)

class Birthdaysponsor(models.Model):

    def __unicode__(self):
        return self.donators_name+" "+self.birthday_person_name

    bid = models.AutoField(primary_key=True)
    donators_name = models.CharField(max_length=200)
    birthday_person_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    orphanage = models.ForeignKey(Orphanage)
# Create your models here.
