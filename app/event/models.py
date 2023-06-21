from django.db import models


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
    booking_open_window = models.DateTimeField()
    event_date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Updated field

    def __str__(self):
        """ String Representation of Event Object """
        return self.title
