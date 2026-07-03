from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
