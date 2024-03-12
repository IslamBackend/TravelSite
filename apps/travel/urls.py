from django.urls import path

from apps.travel.views import TravelListCreateAPIView, TravelRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('travel/', TravelListCreateAPIView.as_view()),
    path('travel/<str:slug>/', TravelRetrieveUpdateDestroyAPIView.as_view()),
]
