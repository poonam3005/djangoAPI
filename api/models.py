from django.db import models

# Create your models here.


class TEmployee(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    company = models.ForeignKey(
        "MCompany", on_delete=models.CASCADE, blank=True, null=True
    )
    department = models.ForeignKey(
        "MDepartment", on_delete=models.CASCADE, blank=True, null=True
    )

        
    def __str__(self):
        return str(self.name)


class MCompany(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)


class MDepartment(models.Model):
    name = models.CharField(max_length=100)


        
    def __str__(self):
        return str(self.name)

    