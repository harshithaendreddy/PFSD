from django.db import models

# Create your models here.
class Admin(models.Model): #Admin is name of the class
    id : models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,blank=False,unique=True)
    password=models.CharField(max_length=12,blank=False)
    class Meta:
       db_table = "ttmadmin_table"  #This is name of the table in database if this is not given admin willl be the table name
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=40, blank=False, unique=True)
    phno = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)
    class Meta:
        db_table = "regiter_table"

class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    tourcode = models.CharField(max_length=10, blank=False)
    tourname = models.CharField(max_length=30, blank=False)
    tourpackage = models.CharField(max_length=30,blank=False)
    desc = models.CharField(max_length=35,blank=False)
    class Meta:
        db_table = "package_table"
