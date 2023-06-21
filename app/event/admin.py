from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    """ Event Admin Model configuration """
    list_display = (
        'title',
        'event_date_time',
        'max_seats',
        'booking_open_window',
        'status'
    )
    date_hierarchy = 'event_date_time'
