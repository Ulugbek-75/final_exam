from django.contrib import admin

from room_app.models import Room, Resident, Availability


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'capacity', 'resident']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'type', 'capacity']
    list_filter = ['type', 'capacity']
    autocomplete_fields = ['resident']


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'start', 'end']
    list_display_links = ['id', 'room']
    search_fields = ['room', 'start', 'end']
    list_filter = ['start', 'end']
    autocomplete_fields = ['room']

