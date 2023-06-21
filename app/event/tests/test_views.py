from collections import OrderedDict
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from event.models import Events
from event.serializers import EventSerializer

ADMIN_EVENT_ENDPOINT = '/api/admin/events/'
EVENT_ENDPOINT = '/api/events/'


def create_event(**params):
    """ Create and return a sample event """
    defaults = {
        'title': 'Event 1',
        'description': 'Event description',
        'event_type': 'online',
        'max_seats': 100,
        'booking_open_window': '2023-06-23T10:00:00Z',
        'event_date_time': '2023-07-02T18:00:00Z',
        'price': '10.00',
    }
    defaults.update(params)
    return Events.objects.create(**defaults)


def create_user(**params):
    """ Create and return a sample user """
    password = params.pop('password')
    user = get_user_model().objects.create(
        first_name='Test',
        last_name='Name',
        **params,
    )
    user.set_password(password)
    user.save()
    return user


class PublicAdminEventApiTest(TestCase):
    """ Test Admin Event API is publicly available """
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """ Test unauthenticated request """
        self.client.logout()
        response = self.client.get(ADMIN_EVENT_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UnauthorizedAdminEventApiTest(TestCase):
    """ Test Admin Event API is accessible to unauthorized user """

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='admin@example.com', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_unauthorized_user(self):
        """ Test unauthenticated request """
        self.client.logout()
        response = self.client.get(ADMIN_EVENT_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AdminEventApiTest(TestCase):
    """ Test Admin Event API """

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email='admin@example.com',
            password='testpass',
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

    def test_retrive_events(self):
        create_event()
        create_event()
        response = self.client.get(ADMIN_EVENT_ENDPOINT)
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_event(self):
        event = create_event()
        payload = event.__dict__
        response = self.client.post(ADMIN_EVENT_ENDPOINT, payload)
        event = Events.objects.all().last()
        serializer = EventSerializer(event)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_update_event(self):
        event = create_event(title='Updated Title')
        payload = event.__dict__
        response = self.client.put(f'{ADMIN_EVENT_ENDPOINT}{event.id}/', payload)
        serializer = EventSerializer(event)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_delete_event(self):
        event = create_event()
        response = self.client.delete(f'{ADMIN_EVENT_ENDPOINT}{event.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Events.objects.filter(id=event.id).exists())


class UnAuthorizedEventApiTest(TestCase):
    """ Test unauthorized Event API """

    def setUp(self):
        self.client = APIClient()

    def test_unauthorize_list_events(self):
        create_event()
        create_event()
        response = self.client.get(EVENT_ENDPOINT)
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_unauthorize_retrive_events(self):
        create_event()
        response = self.client.get(EVENT_ENDPOINT)
        events = Events.objects.all().last()
        serializer = EventSerializer(events)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], serializer.data)


class AuthorizedEventApiTest(TestCase):
    """ Test Authorized Event API """

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email='admin@example.com',
            password='testpass',
            is_staff=False
        )
        self.client.force_authenticate(user=self.user)

    def test_authorize_list_events(self):
        create_event()
        create_event()
        response = self.client.get(EVENT_ENDPOINT)
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_authorize_retrive_events(self):
        create_event()
        response = self.client.get(EVENT_ENDPOINT)
        events = Events.objects.all().last()
        serializer = EventSerializer(events)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], serializer.data)
