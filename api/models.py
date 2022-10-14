from django.db import models

# Create your models here.
   
    
class Employee(models.Model):
    name =  models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)    
    gender = models.CharField(max_length=10)
    company = models.ForeignKey("Company", related_name="cmp",on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.id)
    

class Company(models.Model):
    name =  models.CharField(max_length = 100)
    location = models.CharField(max_length = 100) 
    
    def __str__(self):
        return str(self.name)