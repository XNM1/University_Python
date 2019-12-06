from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor


def index(request):
    return render(request, "index.html")

def sensor(request, id):
    sensor = Sensor.objects.filter(id=id).values()
    return render(request, "sensor.html", context={"sensor": sensor})

def sensors(request):
    sensors = Sensor.objects.all()
    return render(request, "sensors.html", context={"sensors": sensors})
