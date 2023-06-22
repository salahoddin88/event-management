from django.contrib import admin
from .models import (Events, Tickets)


class TicketInlines(admin.TabularInline):
    """ Inlines for Event Tickets """
    model = Tickets
    extra = 0


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    """ Event Admin Model configuration """
    list_display = (
        'title',
        'event_date_time',
        'max_seats',
        'booking_open_window_start',
        'booking_open_window_end',
        'status'
    )
    date_hierarchy = 'event_date_time'
    inlines = (TicketInlines, )
    search_fields = ('title', )
    list_filter = ('event_type', )
