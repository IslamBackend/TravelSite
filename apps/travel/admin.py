from django.contrib import admin

from apps.travel.models import Housing, HousingImage, RoomImage, Room, HousingReview


class HousingImageInline(admin.TabularInline):
    model = HousingImage
    min_num = 3
    max_num = 20
    extra = 0

    class Meta:
        model = HousingImage
        fields = '__all__'


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    list_display = ('housing_name', 'region', 'stars', 'address', 'housing_type')
    list_filter = ('housing_type', 'region', 'stars')
    search_fields = ('housing_name', 'address')
    prepopulated_fields = {'slug': ('housing_name',)}
    inlines = (HousingImageInline,)


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    min_num = 3
    max_num = 20
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('housing', 'room_name', 'price_per_night', 'room_area')
    list_filter = ('housing', 'room_name',)
    search_fields = ('housing__housing_name', 'room_name')
    inlines = (RoomImageInline,)


@admin.register(HousingReview)
class HousingReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'housing', 'created_at')
    list_filter = ('housing',)
