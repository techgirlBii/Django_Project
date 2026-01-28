from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)


    def __str__(self):
        return self.firstname
