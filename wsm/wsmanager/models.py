from django.db import models

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=255)

class Station(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	country = models.ForeignKey(Country)
	lat = models.FloatField()
	lng = models.FloatField()
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

class Parking(models.Model):
	name = models.CharField(max_length=255)
	lat = models.FloatField()
	lng = models.FloatField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

class Price(models.Model):
	name = models.CharField(max_length=255)
	amount = models.FloatField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

class Region(models.Model):
	name = models.CharField(max_length=255)
	country = models.ForeignKey(Country)

class Slope(models.Model):
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=6)
	opened = models.BooleanField()
	kms = models.FloatField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

