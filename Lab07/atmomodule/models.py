from django.db import models

class SensorCategory(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    create_date = models.DateField()
    name = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    category = models.ForeignKey(SensorCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AtmoSnapshot(models.Model):
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)
    temperature = models.FloatField()
    pressure = models.FloatField()
    co2_level = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + " " + str(self.time)
