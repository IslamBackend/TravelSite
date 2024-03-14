from django.db.models import Avg
from rest_framework import serializers

from apps.travel.models import Housing, Room, RoomImage, HousingReview


class HousingListSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'image')


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


class HousingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingReview
        fields = ('id', 'user', 'housing', 'comment', 'created_at', 'cleanliness_rating', 'comfort_rating',
                  'staff_rating', 'value_for_money_rating', 'food_rating', 'location_rating')
        read_only_fields = ('user',)


class HousingDetailSerializer(serializers.ModelSerializer):
    rooms = RoomListSerializer(read_only=True, many=True)
    reviews = HousingReviewSerializer(read_only=True, many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Housing
        fields = ('housing_name', 'average_rating', 'housing_type', 'address', 'region', 'stars',
                  'check_in_time_start', 'check_in_time_end', 'check_out_time_start', 'check_out_time_end',
                  'rooms', 'reviews')

    def get_average_rating(self, obj):
        average_ratings = HousingReview.objects.filter(housing=obj).aggregate(
            Avg('cleanliness_rating'),
            Avg('comfort_rating'),
            Avg('staff_rating'),
            Avg('value_for_money_rating'),
            Avg('food_rating'),
            Avg('location_rating')
        )
        print(HousingReview.staff_rating)
        total_ratings = sum(average_ratings.values()) / len(average_ratings)
        return round(total_ratings)


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = ('id', 'housing', 'room_images', 'room_name', 'price_per_night', 'room_area', 'bedrooms', 'num_rooms',
                  'free_cancellation_anytime')
