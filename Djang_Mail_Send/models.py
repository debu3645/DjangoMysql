from __future__ import unicode_literals

from django.db import models

# Create your models here.
class test(models.Model):
	My_Description = models.TextField()
	#abc = models.TextField()
	First_Name = models.CharField(max_length=30, null=True)
	Last_Name = models.CharField(max_length=30, null=True)

class Myproject(models.Model):
	
	Title = models.CharField(max_length=30, null=True)
	description = models.CharField(max_length=100, null=True)
	client = models.CharField(max_length=100, null=True)

class Vineettable1(models.Model):
	
	Name = models.CharField(max_length=30, null=True)
	Role = models.CharField(max_length=100, null=True)
	section = models.CharField(max_length=100, null=True)

class universitydb(models.Model):
	
	Name = models.CharField(max_length=5, null=True)
	Address = models.CharField(max_length=10, null=True)
	Role = models.CharField(max_length=3, null=True)
	Mobile = models.CharField(max_length=5, null=True)

class collegedb(models.Model):
	
	Name = models.CharField(max_length=5, null=True)
	Address = models.CharField(max_length=10, null=True)	

class guestdb(models.Model):
	
	Name = models.CharField(max_length=5, null=True)
	Age = models.CharField(max_length=2, null=True)
	visits = models.ManyToManyField(collegedb, related_name='collegerelate')

class vinymysqlemp(models.Model):
	
	empname = models.CharField(max_length=20, null=True)
	empid = models.CharField(max_length=20, null=True)
	empsal = models.CharField(max_length=20, null=True)

class Postxx(models.Model):
	title = models.CharField(
			max_length=100,null=True)