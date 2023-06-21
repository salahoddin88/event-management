from rest_framework import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
            'title',
            'description',
            'event_type',
            'max_seats',
            'booking_open_window',
            'event_date_time',
            'price',
        )
        extra_kwargs = {
            'created_date': {'readonly': True},
            'updated_date': {'readonly': True}
        }
