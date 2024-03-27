from django.contrib import admin
from room_app.models import Room, RoomAvailability, BookingRoom


admin.site.register(Room)
admin.site.register(RoomAvailability)
admin.site.register(BookingRoom)