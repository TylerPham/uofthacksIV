"""Base models"""
from django.db import models

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('job name', max_length=50)
    company_id = ForeignKeyField(Company)
    url = models.CharField()
    description = models.CharField()
    still_active = models.CharField()

class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField()
	location_id = ForeignKeyField(Location)

class Location(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = DecimalField()
	longitude = DecimalField()
	city = models.CharField()
	country = models.CharField()

class Rating(models.Model):
	id = models.AutoField(primary_key=True)
	score = IntegerField()
	company_id = ForeignKeyField(Company)

class Distance(models.Model):
    distance_id = models.AutoField(primary_key=True)
    center_id = ForeignKeyField(Location)
    location_id = ForeignKeyField(Location)
    location_to_center = DecimalField()

