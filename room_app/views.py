from rest_framework import generics
from .pagination import CustomPagination
from . import serializers
from .models import Room, Availability
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status
from datetime import datetime, date, timezone


class RoomListView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        search_param = self.request.query_params.get('search', None)
        type_param = self.request.query_params.get('type', None)

        if search_param:
            queryset = queryset.filter(Q(name__icontains=search_param))

        if type_param:
            queryset = queryset.filter(type=type_param)

        return queryset


class RoomDetailView(APIView):
    def get(self, request, pk: int) -> Room:
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "topilmadi"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = serializers.RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomAvailabilityView(APIView):
    def get(self, request, pk: int) -> Response:
        # Get room object
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response({'error': 'topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        # Get date parameter from query string
        date_str = request.GET.get('date')

        if date_str:
            try:
                query_date = datetime.strptime(date_str, '%d-%m-%Y').date()
                query_date_str = date_str
            except ValueError:
                return Response({'error': 'noto\'g\'ri sana formati'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            query_date = date.today()
            query_date_str = query_date.strftime('%d-%m-%Y')

        # Get availabilities based on room and query_date
        availabilities = Availability.objects.filter(room=room, start__date=query_date)

        # Get the booked time ranges
        booked_ranges = [(availability.start.replace(tzinfo=timezone.utc), availability.end.replace(tzinfo=timezone.utc)) for availability in availabilities]

        # Calculate the available time ranges
        start_of_day = datetime.combine(query_date, datetime.min.time()).replace(tzinfo=timezone.utc)
        end_of_day = datetime.combine(query_date, datetime.max.time()).replace(tzinfo=timezone.utc)
        available_ranges = []

        # Check for available ranges within the day
        if len(booked_ranges) == 0:
            available_ranges.append((start_of_day, end_of_day))
        else:
            if start_of_day < booked_ranges[0][0]:
                available_ranges.append((start_of_day, booked_ranges[0][0]))

            for i in range(len(booked_ranges) - 1):
                if booked_ranges[i][1] < booked_ranges[i + 1][0]:
                    available_ranges.append((booked_ranges[i][1], booked_ranges[i + 1][0]))

            if booked_ranges[-1][1] < end_of_day:
                available_ranges.append((booked_ranges[-1][1], end_of_day))

        formatted_availabilities = []
        for start, end in available_ranges:
            start_datetime = start.strftime('%d-%m-%Y %H:%M:%S')
            end_datetime = end.strftime('%d-%m-%Y %H:%M:%S')
            formatted_availabilities.append({
                'start': start_datetime,
                'end': end_datetime
            })

        return Response(formatted_availabilities, status=status.HTTP_200_OK)

    def put(self, request, pk: int) -> Response:
        # Get room object
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response({'error': 'topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        # Get data from request
        data = request.data

        # Update room availability
        serializer = serializers.AvailabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save(room=room)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomReservation(APIView):
    def post(self, request, pk):
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {'error': 'topilmadi'}, status=status.HTTP_404_NOT_FOUND
            )
        resident_data = request.data.get('resident', None)
        start_time = request.data.get('start', None)
        end_time = request.data.get('end', None)

        if not resident_data or not start_time or not end_time:
            return Response({'error': "malumotlar to'liq kiritilmadi"}, status.HTTP_400_BAD_REQUEST)

        try:
            start_datetime = datetime.strptime(start_time, '%d-%m-%Y %H:%M:%S')
            end_datetime = datetime.strptime(end_time, '%d-%m-%Y %H:%M:%S')
        except ValueError:
            return Response({'error': "noto'g'ri vaqt formati"}, status.HTTP_400_BAD_REQUEST)

        if Availability.objects.filter(room=room, start__lt=end_datetime, end__gt=start_datetime).exists():
            return Response({'error': "uzr, siz tanlagan vaqtda xona band"}, status.HTTP_410_GONE)

        resident_serializer = serializers.ResidentSerializer(data=resident_data)
        if resident_serializer.is_valid():
            resident = resident_serializer.save()
            room.resident = resident
            room.save()

            availability = Availability.objects.create(room=room, start=start_datetime, end=end_datetime)
            availability.save()

            return Response({'message': 'xona muvaffaqiyatli band qilindi'}, status=status.HTTP_201_CREATED)
        else:
            return Response(resident_serializer.errors)



