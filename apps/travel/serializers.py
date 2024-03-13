from rest_framework import serializers

from apps.travel.models import Housing, Room, RoomImage


class TravelListSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Housing
        fields = ('id', 'slug', 'housing_name', 'region', 'first_image', 'stars', 'address')

    def get_first_image(self, obj):
        request = self.context.get('request')
        first_image_instance = obj.housing_images.first()

        if first_image_instance:
            image_url = first_image_instance.image.url
            full_image_url = request.build_absolute_uri(image_url)
            return full_image_url

        return None


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = "__all__"


class TravelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = ('housing_name', 'housing_type', 'address', 'region', 'stars',
                  'check_in_time_start', 'check_in_time_end', 'check_out_time_start', 'check_out_time_end')


class RoomListSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('id', 'room_name', 'first_image', 'price_per_night', 'free_cancellation_anytime')

    def get_first_image(self, obj):
        request = self.context.get('request')
        first_image_instance = obj.room_images.first()

        if first_image_instance:
            image_url = first_image_instance.image.url
            full_image_url = request.build_absolute_uri(image_url)
            return full_image_url

        return None


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = ('id', 'housing', 'room_images', 'room_name', 'price_per_night', 'room_area', 'bedrooms', 'num_rooms',
                  'free_cancellation_anytime')
