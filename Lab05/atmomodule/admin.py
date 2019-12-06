from django.contrib import admin
from .models import SensorCategory
from .models import Sensor
from .models import AtmoSnapshot


# Register your models here.
admin.site.register(SensorCategory)
admin.site.register(Sensor)
admin.site.register(AtmoSnapshot)