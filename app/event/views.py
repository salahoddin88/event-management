from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer
from .models import Events


class EventViewSet(ModelViewSet):
    """ REST API for Admin to CRUD Event """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    serializer_class = EventSerializer
    queryset = Events.objects.all()


class ViewEventViewSet(ModelViewSet):
    """ Event Get API to serve list and retrieve to customer """
    serializer_class = EventSerializer
    queryset = Events.objects.filter(status=True)
    http_methods = ['get']
