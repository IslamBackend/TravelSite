from django.urls import path

from apps.travel.views import HousingListCreateAPIView, HousingRetrieveUpdateDestroyAPIView, RoomListCreateAPIView, \
    RoomRetrieveUpdateDestroyAPIView, HousingReviewsCreateAPIView

urlpatterns = [
    path('housing/', HousingListCreateAPIView.as_view()),
    path('housing/<str:slug>/', HousingRetrieveUpdateDestroyAPIView.as_view()),
    path('rooms/', RoomListCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view()),
    path('reviews/', HousingReviewsCreateAPIView.as_view()),
]
