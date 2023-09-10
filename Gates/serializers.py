
from Gates.models import*
from rest_framework import serializers

class SerializeRailwaysiding(serializers.ModelSerializer):
    class Meta:
        model=Railwaysiding
        fields='__all__'

class SerializeIngate(serializers.ModelSerializer):
    class Meta:
        model=Ingate
        fields='__all__'
class SerializeOutgate(serializers.ModelSerializer):
    class Meta:
        model=Outgate
        fields='__all__'

class SerializeFuelgate(serializers.ModelSerializer):
    class Meta:
        model=Fuelgate
        fields='__all__'
