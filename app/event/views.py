from rest_framework import (permissions, response, status)
from rest_framework.generics import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import (ModelViewSet, ViewSet)
from .serializers import (
    EventSerializer,
    ListTicketSerializer,
    POSTTicketSerializer,
    RetrieveTicketSerializer
)
from .models import (Events, Tickets)


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
    http_method_names = ['get']


class TicketsView(ViewSet):
    """ Event Tickets API """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ListTicketSerializer
    queryset = Tickets.objects.all()

    def list(self, request):
        queryset = Tickets.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk):
        event = get_object_or_404(self.queryset, pk=pk, user=request.user)
        serializer = RetrieveTicketSerializer(event)
        return response.Response(serializer.data)

    def create(self, request):
        serializer = POSTTicketSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.validated_data.get('event')
            ticket = Tickets.objects.create(
                event=event,
                user=request.user,
            )
            serializer = self.serializer_class(ticket)
            return response.Response(serializer.data)
        return response.Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        event = get_object_or_404(self.queryset, pk=pk, user=request.user)
        event.delete()
        return response.Response()
