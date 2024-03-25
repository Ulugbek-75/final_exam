from django.urls import path
from . import views


urlpatterns = [
    path('room_app/', views.RoomListView.as_view(), name='rooms_list'),
    path('room_app/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('room_app/<int:pk>/availability/', views.RoomAvailabilityView.as_view()),
    path('room_app/<int:pk>/book/', views.RoomReservation.as_view()),
]