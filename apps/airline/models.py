from django.db import models
from apps.plane.models import Plane

class Airline(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    planes = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'