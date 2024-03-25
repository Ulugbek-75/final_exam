from django.urls import path
from . import views


urlpatterns = [
    path('room_app/', views.RoomListView.as_view(), name='rooms_list'),
    path('room_app/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('room_app/<int:pk>/availability/', views.RoomAvailabilityView.as_view(), name='room_availability'),
    path('room_app/<int:pk>/book/', views.RoomBookView.as_view(), name='room_book'),
    path('room_app/<int:pk>/cancel/', views.RoomCancelView.as_view(), name='room_cancel'),
    path('room_app/<int:pk>/check/', views.RoomCheckView.as_view(), name='room_check'),
    path('room_app/<int:pk>/checkin/', views.RoomCheckInView.as_view(), name='room_checkin'),
    path('room_app/<int:pk>/checkout/', views.RoomCheckOutView.as_view(), name='room_checkout'),
    path('room_app/<int:pk>/clean/', views.RoomCleanView.as_view(), name='room_clean'),
    path('room_app/<int:pk>/dirty/', views.RoomDirtyView.as_view(), name='room_dirty'),
]