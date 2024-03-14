from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from apps.travel.models import Housing, Room, HousingReview
from apps.travel.serializers import (HousingListSerializer, HousingDetailSerializer,
                                     RoomListSerializer, RoomDetailSerializer, HousingReviewSerializer)


class HousingListCreateAPIView(ListCreateAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingListSerializer
        return self.serializer_class


class HousingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingDetailSerializer
    lookup_field = 'slug'


class RoomListCreateAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomListSerializer
        return self.serializer_class


class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class HousingReviewsCreateAPIView(CreateAPIView):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)
