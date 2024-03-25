from django.db import models
from .enum import RoomType


class Resident(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=RoomType.choices())
    capacity = models.IntegerField()
    resident = models.ForeignKey(Resident, blank=True, null=True, on_delete=models.SET_NULL)


def __str__(self):
    return self.name



class Availability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.start} || {self.end}"

    class Meta:
        verbose_name = 'Availability'
        verbose_name_plural = 'Availabilities'
