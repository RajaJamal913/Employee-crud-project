# employees/models.py
from django.db import models # type: ignore

class Employee_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
