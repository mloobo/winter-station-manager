from django.contrib import admin
from .models import *
# Register your models here.

class StationAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'country', 'lat', 'lng', 'created',
		'updated')
	list_filter = ['created', 'updated', 'country']
	search_fields = ['name']

class SlopeAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'color', 'created', 'updated')
	list_filter = ['created', 'updated']
	search_fields = ['name']

admin.site.register(Station, StationAdmin)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Parking)
admin.site.register(Price)
admin.site.register(Slope)