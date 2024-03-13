from django.urls import path

from apps.travel.views import TravelListCreateAPIView, TravelRetrieveUpdateDestroyAPIView, RoomListCreateAPIView, \
    RoomRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('travel/', TravelListCreateAPIView.as_view()),
    path('travel/<str:slug>/', TravelRetrieveUpdateDestroyAPIView.as_view()),
    path('room/', RoomListCreateAPIView.as_view()),
    path('room/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view()),
]
