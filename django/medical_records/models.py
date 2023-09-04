from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=50)
    first_consult = models.DateTimeField(auto_now=True)
    phone_number = models.IntegerField()