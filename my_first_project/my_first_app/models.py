from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    description = models.TextField()
    hobby = models.CharField(null=True, max_length=100)
    phone = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.name} {self.lastname}"
    
class Content(models.Model):
     name = models.CharField(max_length=255)
     lastname = models.CharField(max_length=255)
     description = models.TextField()
     hobby = models.CharField(null=True, max_length=100)
     phone = models.IntegerField(null=True)

     def __str__(self):
            return self.name