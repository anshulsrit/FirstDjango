from django.db import models

# Create your models here.
class Simpleformdata(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(max_length=140)
    religion = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' %(self.firstname ,self.lastname)



