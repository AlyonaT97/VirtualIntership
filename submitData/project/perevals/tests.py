from django.urls import reverse
from rest_framework import status

from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Perevals, Coords, Users, Level
from .serializers import PerevalsSerializer


class MountApiTestCase(APITestCase):

    def setUp(self):
        user_1 = Users.objects.create(email='test@mail.ru', full_name='Smith Max', phone=1234)
        user_2 = Users.objects.create(email='test2@gmail.com', full_name='Gwen Stephany', phone=5678)
        coord_1 = Coords.objects.create(latitude=4.3467, longitude=6.3209, height=3453)
        coord_2 = Coords.objects.create(latitude=47.9237, longitude=23.4572, height=4579)
        level_1 = Level.objects.create(winter='3a', summer='2a', autumn='2b', spring='2b')
        level_2 = Level.objects.create(winter='4a', summer='3a', autumn='3b', spring='3b')
        self.mount_1 = Perevals.objects.create(beautyTitle='beautyTitle1', title='title1', other_titles='other_titles1',
                                               connect='', status='PN', level_id=level_1, user_id=user_1, coord_id=coord_1)
        self.mount_2 = Perevals.objects.create(beautyTitle='beautyTitle2', title='title2', other_titles='other_titles2',
                                               connect='', status='NW', level_id=level_2, user_id=user_2, coord_id=coord_2)

    def test_get_list(self):
        url = reverse('perevals_list')
        response = self.client.get(url)
        serializer_data = PerevalsSerializer([self.mount_1, self.mount_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('pereval_detail', args=(self.mount_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalsSerializer(self.mount_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class MountSerializerTestCase(TestCase):

    def setUp(self):
        user_1 = Users.objects.create(email='test@mail.ru', full_name='Smith Max', phone=1234)
        user_2 = Users.objects.create(email='test2@gmail.com', full_name='Gwen Stephany', phone=5678)
        coord_1 = Coords.objects.create(latitude=4.3467, longitude=6.3209, height=3453)
        coord_2 = Coords.objects.create(latitude=47.9237, longitude=23.4572, height=4579)
        level_1 = Level.objects.create(winter='3a', summer='2a', autumn='2b', spring='2b')
        level_2 = Level.objects.create(winter='4a', summer='3a', autumn='3b', spring='3b')
        self.mount_1 = Perevals.objects.create(beautyTitle='beautyTitle1', title='title1', other_titles='other_titles1',
                                               connect='', status='PN', level_id=level_1, user_id=user_1,
                                               coord_id=coord_1)
        self.mount_2 = Perevals.objects.create(beautyTitle='beautyTitle2', title='title2', other_titles='other_titles2',
                                               connect='', status='NW', level_id=level_2, user_id=user_2,
                                               coord_id=coord_2)

    def test_check(self):
        serializer_data = PerevalsSerializer([self.mount_1, self.mount_2], many=True).data

        expected_data = [
            {
                'id': 1,
                'beautyTitle': 'beautyTitle1',
                'title': 'title1',
                'other_titles': 'other_titles1',
                'connect': '',
                'status': 'PN',
                'add_time': self.mount_1.add_time.strftime('%Y-%m-%dT%H:%M:%S.$fZ'),
                'level_id': {
                    'id': 1,
                    'winter': '3a',
                    'summer': '2a',
                    'autumn': '2b',
                    'spring': '2b'
                },
                'user_id': {
                    'id': 2,
                    'email': 'test@mail.ru',
                    'full_name': 'Smith Max',
                    'phone': 1234
                },
                'coord_id': {
                    'latitude': 4.3467,
                    'longitude': 6.3209,
                    'height': 3453
                },
                'images': []
            },
            {
                'id': 2,
                'beautyTitle': 'beautyTitle2',
                'title': 'title2',
                'other_titles': 'other_titles2',
                'connect': '',
                'status': 'NW',
                'add_time': self.mount_2.add_time.strftime('%Y-%m-%dT%H:%M:%S.$fZ'),
                'level_id': {
                    'id': 2,
                    'winter': '4a',
                    'summer': '3a',
                    'autumn': '3b',
                    'spring': '3b'
                },
                'user_id': {
                    'id': 3,
                    'email': 'test2@gmail.com',
                    'full_name': 'Gwen Stephany',
                    'phone': 5678
                },
                'coord_id': {
                    'latitude': 47.9237,
                    'longitude': 23.4572,
                    'height': 4579
                },
                'images': []
            }
        ]

        self.assertEqual(serializer_data, expected_data)




