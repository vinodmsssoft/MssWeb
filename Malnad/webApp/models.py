from django.db import models

# Create your models here.



class Contact (models.Model):
    name    = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email   = models.EmailField()
    subject = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    class Meta:
        db_table = 'contact'
