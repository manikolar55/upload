from django.db import models
from django import forms
# Create your models here.
from django_countries.fields import CountryField

class Foo(models.Model):
    country = CountryField()
class server_loogin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
class country_name(models.Model):
    CountryID=models.IntegerField(primary_key=True)
    CountryName = models.CharField(max_length=50)
    TwoCharCountryCode=models.CharField(max_length=2)
    ThreeCharCountryCode=models.CharField(max_length=3)



    def __str__(self):
        return self.CountryName
class city_names(models.Model):
    countryname=models.ForeignKey(country_name,on_delete=models.CASCADE)
    cityname=models.CharField(max_length=50)

#server add production model
class server_products(models.Model):
    # img=models.ImageField(upload_to='images')
    img = models.ImageField(upload_to='images')
    desc=models.CharField(max_length=100)
    price=models.IntegerField()
    name=models.CharField(max_length=20)
class user_signup(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
class serverice_table(models.Model):
    services=models.CharField(max_length=20)
class orders(models.Model):
    username=models.CharField(max_length=20)
    product_names=models.CharField(max_length=20)
    product_descriptions=models.CharField(max_length=20)
    product_service=models.CharField(max_length=20)
    approved=models.CharField(max_length=20)
    email=models.EmailField()
class approveds_orders(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    approved=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)

