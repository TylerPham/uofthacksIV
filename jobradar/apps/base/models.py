"""Base models"""
from django.db import models

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('job name', max_length=50)
    company_id = models.ForeignKey('Company')
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    still_active = models.BooleanField()

class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	location_id = models.ForeignKey('Location')

class Location(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = models.DecimalField(decimal_places=12, max_digits=15)
	longitude = models.DecimalField(decimal_places=12, max_digits=15)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=20)

class Rating(models.Model):
	id = models.AutoField(primary_key=True)
	score = models.IntegerField()
	company_id = models.ForeignKey('Company')

class Distance(models.Model):
    distance_id = models.AutoField(primary_key=True)
    center_id = models.ForeignKey('Location', related_name='center_location')
    location_id = models.ForeignKey('Location', related_name='loc_location')
    location_to_center = models.DecimalField(decimal_places=12, max_digits=15)
