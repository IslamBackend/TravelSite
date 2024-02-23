from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from TravelSite.settings.swagger import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
] + swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)