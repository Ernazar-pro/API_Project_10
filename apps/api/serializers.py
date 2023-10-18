from apps.airline.models import Airline
from apps.flight.models import Flight
from apps.plane.models import Plane
from rest_framework.serializers import *

class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PlaneSerializer(ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'
