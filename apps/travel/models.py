from django.db import models
from django.utils.text import slugify

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
