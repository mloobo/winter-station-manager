from django.db import models

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Status(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Station(models.Model):
	name = models.CharField(max_length=255)
	country = models.ForeignKey(Country)
	status = models.ForeignKey(Status)
	lat = models.FloatField()
	lng = models.FloatField()
	web_url = models.CharField(max_length=255, default='', blank=True)
	slopes_map_url = models.CharField(max_length=255, default='', blank=True)
	url_snowforecast = models.CharField(max_length=255, default='#', blank=True)
	url_skipass = models.CharField(max_length=255, default='#', blank=True)
	phone = models.CharField(max_length=255, default='')
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

class Currency(models.Model):
	name = models.CharField(max_length=255, default='&euro;')

	def __str__(self):
		return self.name


class Price(models.Model):
	name = models.CharField(max_length=255)
	amount = models.FloatField()
	station = models.ForeignKey(Station)
	currency = models.ForeignKey(Currency, default=1)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return self.station.name + ' - ' + self.name

class Region(models.Model):
	name = models.CharField(max_length=255)
	country = models.ForeignKey(Country)

	def __str__(self):
		return self.name

class Webcam(models.Model):
	name = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	station = models.ForeignKey(Station)

	def __str__(self):
		return self.station.name + '-' + self.name

class SlopeType(models.Model):
	COLORS = (
		('#109231', 'Green'),
		('#435993', 'Blue'),
		('#C6190B', 'Red'),
		('#000000', 'Black'),
	)

	name = models.CharField(max_length=255)
	long_name = models.CharField(max_length=255, default='')
	color = models.CharField(max_length=7, choices=COLORS, default='#109231')
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return self.long_name

class StationSlopeStatus(models.Model):
	slopetype = models.ForeignKey(SlopeType)
	station = models.ForeignKey(Station)
	total = models.IntegerField(default=0)
	closed = models.IntegerField(default=0)
	opened = models.IntegerField(default=0)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return "{0} - {1} - Total {2} - Closed {3} - Opened: {4}".format(self.station.name, self.slopetype.long_name, self.total, self.closed, self.opened)

class Slope(models.Model):
	COLORS = (
		('g', 'Green'),
		('b', 'Blue'),
		('r', 'Red'),
		('n', 'Black'),
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

class Snowpark(models.Model):
	name = models.CharField(max_length=255)
	opened = models.BooleanField()
	station = models.ForeignKey(Station)
	created = models.DateTimeField("date created")
	updated = models.DateTimeField("date updated")

	def __str__(self):
		return self.station.name + ' - ' + self.name