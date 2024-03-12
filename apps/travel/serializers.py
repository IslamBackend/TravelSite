from rest_framework import serializers

from apps.travel.models import Housing


class TravelListSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Housing
        fields = ('id', 'housing_name', 'region', 'first_image', 'stars', 'address')

    def get_first_image(self, obj):
        first_image_instance = obj.housing_images.first()
        if first_image_instance:
            return first_image_instance.image.url
        else:
            return None


class TravelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = ('housing_name', 'housing_type', 'address', 'region', 'stars',
                  'check_in_time_start', 'check_in_time_end', 'check_out_time_start', 'check_out_time_end')
