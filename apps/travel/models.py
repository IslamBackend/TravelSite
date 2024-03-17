from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from apps.travel.constants import *


class Housing(models.Model):
    housing_name = models.CharField(max_length=255, verbose_name='Название места жительства')
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Человеко-понятный url", blank=True, null=True)
    housing_type = models.CharField(max_length=50, choices=HOUSING_CHOICES, verbose_name="Тип жилья")
    address = models.CharField(max_length=255, verbose_name='Адрес')
    region = models.CharField(max_length=255, choices=DESTINATION_CHOICES, verbose_name='Область')
    stars = models.IntegerField(default=0, choices=STAR_CHOICES, verbose_name='Количество звезд')
    check_in_time_start = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Заезд С")
    check_in_time_end = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Заезд До")
    check_out_time_start = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Отъезд С")
    check_out_time_end = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Отъезд До")

    def __str__(self):
        return f"{self.housing_name}"

    def save(self, *args, **kwargs):
        # Генерация слага на основе названия места жительства
        if not self.slug:
            self.slug = slugify(self.housing_name)

        # Проверка на уникальность слага и добавление уникального суффикса при необходимости
        original_slug = self.slug
        count = 1
        while Housing.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{count}"
            count += 1

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Место жительства'
        verbose_name_plural = 'Места жительства'


class HousingImage(models.Model):
    image = models.ImageField(upload_to='housing', verbose_name="Изображения мест жительств")
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='housing_images', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.housing.housing_name}"


class HousingReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviews',
                             verbose_name="Пользователь")
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Место жительства')
    comment = models.TextField(max_length=500, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    cleanliness_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Чистота')
    comfort_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Комфорт')
    staff_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Персонал')
    value_for_money_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES,
                                                              verbose_name='Цена/Качества')
    food_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Питание')
    location_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Местоположение')

    def __str__(self):
        return f"Отзыв от {self.user} на {self.housing.housing_name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Room(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE,
                                related_name='rooms', verbose_name='Название места жительства')
    room_name = models.CharField(max_length=100, choices=ACCOMMODATION_TYPE_CHOICES, verbose_name='Название номера')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена за ночь")
    num_rooms = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)],
                                    verbose_name="Количество комнат в номере")
    bedrooms = models.CharField(max_length=50, choices=BEDROOM_CHOICES, verbose_name="Количество спален")
    room_area = models.PositiveIntegerField(verbose_name="Площадь комнаты(м²)")
    free_cancellation_anytime = models.BooleanField(default=False, verbose_name='Бесплатное отмена в любое время')

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class RoomImage(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name='room_images', null=True, blank=True)
    image = models.ImageField(upload_to='rooms', verbose_name="Изображения номера", null=True, blank=True)

    def __str__(self):
        return f"Image for {self.room.room_name}"

    class Meta:
        verbose_name = 'Изображение номера'
        verbose_name_plural = 'Изображения номеров'


class WishlistAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Альбом желаний"
        verbose_name_plural = "Альбомы желаний"

    def __str__(self):
        return self.title


class HouseFavorite(models.Model):
    wishlist_album = models.ForeignKey(WishlistAlbum, on_delete=models.CASCADE, related_name='favorites')
    house = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"

    def __str__(self):
        return f"{self.user.username} - {self.house.housing_name}"
