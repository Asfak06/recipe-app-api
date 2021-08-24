from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Polls

from .serializers import PollSerializer


POLLS_URL = reverse('polls:polls-list')


class PollsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_polls(self):
        Polls.objects.create(name="test polls", link='asfak.me')
        res = self.client.get(POLLS_URL)
        polls = Polls.objects.all().order_by('-name')
        serializer = PollSerializer(polls, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
