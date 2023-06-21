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
    event_date = models.DateTimeField()

    def __str__(self):
        """ String Representation of Event Object """
        return self.title


class EventTicket(models.Model):
    """ Event tickets Package """
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        """ String Representation of Event Ticke Package Object """
        return f"{self.event}:{self.title}-{self.price}"


