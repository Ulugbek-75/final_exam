from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from room_app.models import Room
from .serializers import RoomSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', "type", "capacity"]
    filterset_fields = ["type", "capacity"]

    def get_queryset(self):
        return self.queryset


class RoomRetrieveAPIView(RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = "pk"


class RoomDestroyAPIView(DestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


__all__ = ["RoomListAPIView", "RoomRetrieveAPIView", "RoomDestroyAPIView"]