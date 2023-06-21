from django.db import models
from django.contrib.auth import get_user_model


class Events(models.Model):
    """ Events Model """
    EVENT_TYPES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    max_seats = models.PositiveIntegerField()
    booking_open_window_start = models.DateTimeField()
    booking_open_window_end = models.DateTimeField()
    event_date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Updated field

    def __str__(self):
        """ String Representation of Event Object """
        return self.title


class Tickets(models.Model):
    class Meta:
        ordering = ('-event__event_date_time', )
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="user_tickets"
    )
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        """ String Representation of Tickets Object """
        return f'{self.event} {self.user}'


class Payment(models.Model):
    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )
    # Addtional Payment field based on payment gateway

    class Meta:
        abstract = True
