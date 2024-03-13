from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.travel.models import Housing, Room
from apps.travel.serializers import (TravelListSerializer, TravelDetailSerializer,
                                     RoomListSerializer, RoomDetailSerializer)


class TravelListCreateAPIView(ListCreateAPIView):
    queryset = Housing.objects.all()
    serializer_class = TravelDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TravelListSerializer
        return self.serializer_class


class TravelRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Housing.objects.all()
    serializer_class = TravelDetailSerializer
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


