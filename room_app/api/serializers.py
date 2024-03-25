from rest_framework import serializers
from room_app.models import Resident, Availability, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'type', 'capacity']


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['start', 'end']


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ['name', ]


class ResidentDetailSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    availability = AvailabilitySerializer(many=True)

    class Meta:
        model = Resident
        fields = ['name', 'room', 'availability']



