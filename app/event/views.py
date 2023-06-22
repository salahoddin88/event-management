from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework import (
    authentication,
    permissions,
    response,
    status,
    filters
)
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import (ModelViewSet, ViewSet)
from .serializers import (
    EventSerializer,
    RetrieveEventSerializer,
    ListTicketSerializer,
    POSTTicketSerializer,
    RetrieveTicketSerializer
)
from .models import (Events, Tickets)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'search',
                OpenApiTypes.STR,
                description='Search in title and event type',
            ),
            OpenApiParameter(
                'ordering',
                OpenApiTypes.STR,
                description='Order by price ASC and DESC',
            ),
        ]
    )
)
class EventViewSet(ModelViewSet):
    """ REST API for Admin to CRUD Event """
    serializer_class = EventSerializer
    queryset = Events.objects.all()
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'event_type']
    ordering_fields = ['price']

    def retrieve(self, request, pk):
        """ Retrieving event with ticket sold details """
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = RetrieveEventSerializer(event)
        return response.Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'search',
                OpenApiTypes.STR,
                description='Search in title and event type',
            ),
            OpenApiParameter(
                'ordering',
                OpenApiTypes.STR,
                description='Order by price ASC and DESC',
            ),
        ]
    )
)
class ViewEventViewSet(ModelViewSet):
    """ Event Get API to serve list and retrieve to customer """
    serializer_class = EventSerializer
    queryset = Events.objects.filter(status=True)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'event_type']
    ordering_fields = ['price']
    http_method_names = ['get']


class TicketsView(ViewSet):
    """ Event Tickets API """
    serializer_class = POSTTicketSerializer
    queryset = Tickets.objects.all()
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request):
        queryset = Tickets.objects.filter(
            user=request.user
        ).order_by('event__event_date_time')
        serializer = ListTicketSerializer(queryset, many=True)
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
