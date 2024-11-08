from django.db import models

class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True)
    agency_id = models.CharField(max_length=10)
    route_short_name = models.CharField(max_length=100)
    route_long_name = models.CharField(max_length=255)
    route_type = models.IntegerField()

    def __str__(self):
        return f'{self.route_short_name} - {self.route_long_name}'


