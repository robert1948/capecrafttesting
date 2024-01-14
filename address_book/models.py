from django.db import models
"""
Create an address book app with a model called Address that has the following fields:
first_name
last_name
address
city
state
zipcode
phone
email
"""
# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name