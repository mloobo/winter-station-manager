from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the wsmanager index.")

def detail(request, station_id):
    return HttpResponse("You're looking at station %s." % station_id)