from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('admin/events', views.EventViewSet)
router.register('events', views.ViewEventViewSet)
router.register('tickets', views.TicketsView)

urlpatterns = [
    path('', include(router.urls))
]
