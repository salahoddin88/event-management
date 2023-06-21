from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer
from .models import Events


class EventViewSets(ModelViewSet):
    """ Event REST API """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    serializer_class = EventSerializer
    queryset = Events.objects.filter(status=True)
