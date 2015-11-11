from django.db import models

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Station(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	country = models.ForeignKey(Country)
	lat = models.FloatField()
	lng = models.FloatField()
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return self.name

class Parking(models.Model):
	name = models.CharField(max_length=255)
	lat = models.FloatField()
	lng = models.FloatField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return self.name

class Price(models.Model):
	name = models.CharField(max_length=255)
	amount = models.FloatField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length=255)
	country = models.ForeignKey(Country)

	def __str__(self):
		return self.name

class Slope(models.Model):
	COLORS = (
		('g', 'Green'),
		('b', 'Blue'),
		('r', 'Red'),
		('b', 'Black'),
	)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=1, choices=COLORS, default='g')
	opened = models.BooleanField()
	kms = models.FloatField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")


	def __str__(self):
		return self.name