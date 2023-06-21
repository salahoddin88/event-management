from django.utils import timezone
from rest_framework import serializers
from .models import (Events, Tickets)


class EventSerializer(serializers.ModelSerializer):
    """ Event Model Serializer """
    class Meta:
        model = Events
        fields = (
            'id',
            'title',
            'description',
            'event_type',
            'max_seats',
            'booking_open_window_start',
            'booking_open_window_end',
            'event_date_time',
            'price',
        )
        extra_kwargs = {
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True}
        }


class EventListTicketSerializer(serializers.ModelSerializer):
    """ Event Model Serializer """
    class Meta:
        model = Events
        fields = (
            'title',
            'event_type',
            'event_date_time',
            'price',
        )
        extra_kwargs = {
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True}
        }


class ListTicketSerializer(serializers.ModelSerializer):
    """ List Ticket Model GET Serializer """
    event = EventListTicketSerializer()

    class Meta:
        model = Tickets
        fields = (
            'id',
            'event',
            'booking_date',
            'payment_status',
        )


class RetrieveTicketSerializer(serializers.ModelSerializer):
    """ Ticket Model GET Serializer """
    event = EventSerializer()

    class Meta:
        model = Tickets
        fields = (
            'id',
            'event',
            'booking_date',
            'payment_status',
            'user'
        )
        extra_kwargs = {
            'user':  {'read_only': True},
            'payment_status':  {'read_only': True},
            'booking_date':  {'read_only': True},
        }


class POSTTicketSerializer(serializers.ModelSerializer):
    """ Ticket Model POST Serializer """
    class Meta:
        model = Tickets
        fields = (
            'id',
            'event',
        )

    def validate(self, attrs):
        event = attrs['event']
        now = timezone.now()
        if now < event.booking_open_window_start or \
           now >= event.booking_open_window_end:
            raise serializers.ValidationError(
                "Booking is not yet open for this event."
            )
        booked_seats = Tickets.objects.filter(event=event).count()
        if booked_seats >= event.max_seats:
            raise serializers.ValidationError(
                "No more seats available for this event."
            )
        return attrs
