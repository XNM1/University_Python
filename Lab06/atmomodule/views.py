from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, SensorCategory


def index(request):
    return render(request, "index.html")

def sensor(request, id):
    sensor = Sensor.objects.filter(id=id).values()
    category = SensorCategory.objects.filter(id=list(sensor)[0]['category_id']).values()
    return render(request, "sensor.html", context={"sensor": list(sensor)[0], "category": list(category)[0]})

def sensors(request):
    sensors = Sensor.objects.all()
    return render(request, "sensors.html", context={"sensors": list(sensors)})
