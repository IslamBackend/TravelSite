from django.contrib import admin

from apps.travel.models import Housing, HousingImage


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


