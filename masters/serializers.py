
from masters.models import*
from rest_framework import serializers

class SerializeWeighbridge(serializers.ModelSerializer):
    class Meta:
        model=Weighbridge
        fields='__all__'

class SerializeVehicles(serializers.ModelSerializer):
    class Meta:
        model=Vehicles
        fields='__all__'

class SerializeOwners(serializers.ModelSerializer):
    class Meta:
        model=Owners
        fields='__all__'

class SerializeDrivers(serializers.ModelSerializer):
    class Meta:
        model=Drivers
        fields='__all__'

class SerializeLocatios(serializers.ModelSerializer):
    class Meta:
        model=Locations
        fields='__all__'

        