from django.db import models

class Plane(models.Model):
    name = models.CharField(max_length=256)
    characteristics = models.TextField(blank=True, null=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
    
    