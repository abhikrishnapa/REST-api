from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=100) 
    price = models.FloatField()    
    year = models.IntegerField()    
    quantity = models.CharField(max_length=20)   
    
    
    def __str__(self) :
        return self.name