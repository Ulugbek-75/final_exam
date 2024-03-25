from enum import Enum


class RoomType(Enum):
    focus = "focus"
    team = "team"
    conference = "conference"

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)