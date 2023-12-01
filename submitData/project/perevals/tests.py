from django.urls import reverse
from rest_framework import status

from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Perevals, Coords, Users, Level, Images
from .serializers import PerevalsSerializer


class MountApiTestCase(APITestCase):

    def setUp(self):
        user_1 = Users.objects.create(email='test@mail.ru', full_name='Smith Max', phone=1234)
        user_2 = Users.objects.create(email='test2@gmail.com', full_name='Gwen Stephany', phone=5678)
        coord_1 = Coords.objects.create(latitude=4.3467, longitude=6.3209, height=3453)
        coord_2 = Coords.objects.create(latitude=47.9237, longitude=23.4572, height=4579)
        level_1 = Level.objects.create(winter='3a', summer='2a', autumn='2b', spring='2b')
        level_2 = Level.objects.create(winter='4a', summer='3a', autumn='3b', spring='3b')
        self.mount_1 = Perevals.objects.create(beauty_title='beauty_title', title='title1', other_titles='other_titles1',
                                               connect='', status='PN', level_id=level_1, user_id=user_1, coord_id=coord_1)
        self.mount_2 = Perevals.objects.create(beauty_title='beauty_title2', title='title2', other_titles='other_titles2',
                                               connect='', status='NW', level_id=level_2, user_id=user_2, coord_id=coord_2)

        Images.objects.bulk_create(
            [
                Images(title='Title_1', image='https://www.istockphoto.com/ru/фото/перевал-винозе-gm603870390-103682777',
                       pereval_id=self.mount_1),
                Images(title='Title_2', image='https://www.istockphoto.com/ru/фото/перевал-харднот-gm603870438-103682825',
                       pereval_id=self.mount_1)
            ]
        )

        Images.objects.bulk_create(
            [
                Images(title='Title_3', image='https://www.istockphoto.com/ru/фото/камень-пирамида-из-камней-gm471001336-62533536',
                       pereval_id=self.mount_2),
                Images(title='Title_4', image='https://www.istockphoto.com/ru/фото/coniston-выполняют-gm471001332-62533240',
                       pereval_id=self.mount_2)
            ]
        )

    def test_get_perevals_list(self):
        url = reverse('perevals_list')
        response = self.client.get(url)
        perevals = Perevals.objects.all()
        serializer = PerevalsSerializer(perevals, many=True)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_pereval(self):
        url = reverse('pereval_detail', kwargs={'pk': self.mount_1.pk})
        response = self.client.get(url)
        pereval = Perevals.objects.get(pk=self.mount_1.pk)
        serializer = PerevalsSerializer(pereval)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_pereval(self):
        url = reverse('pereval_detail', kwargs={'pk': 51})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class MountSerializerTestCase(TestCase):

    def setUp(self):
        user_1 = Users.objects.create(email='test@mail.ru', full_name='Smith Max', phone=1234)
        user_2 = Users.objects.create(email='test2@gmail.com', full_name='Gwen Stephany', phone=5678)
        coord_1 = Coords.objects.create(latitude=4.3467, longitude=6.3209, height=3453)
        coord_2 = Coords.objects.create(latitude=47.9237, longitude=23.4572, height=4579)
        level_1 = Level.objects.create(winter='3a', summer='2a', autumn='2b', spring='2b')
        level_2 = Level.objects.create(winter='4a', summer='3a', autumn='3b', spring='3b')
        self.mount_1 = Perevals.objects.create(beauty_title='beauty_title', title='title1', other_titles='other_titles1',
                                               connect='', status='PN', level_id=level_1, user_id=user_1,
                                               coord_id=coord_1)
        self.mount_2 = Perevals.objects.create(beauty_title='beauty_title2', title='title2', other_titles='other_titles2',
                                               connect='', status='NW', level_id=level_2, user_id=user_2,
                                               coord_id=coord_2)

        Images.objects.bulk_create(
            [
                Images(title='Title_1',
                       image='https://www.istockphoto.com/ru/фото/перевал-винозе-gm603870390-103682777',
                       pereval_id=self.mount_1),
                Images(title='Title_2',
                       image='https://www.istockphoto.com/ru/фото/перевал-харднот-gm603870438-103682825',
                       pereval_id=self.mount_1)
            ]
        )

        Images.objects.bulk_create(
            [
                Images(title='Title_3',
                       image='https://www.istockphoto.com/ru/фото/камень-пирамида-из-камней-gm471001336-62533536',
                       pereval_id=self.mount_2),
                Images(title='Title_4',
                       image='https://www.istockphoto.com/ru/фото/coniston-выполняют-gm471001332-62533240',
                       pereval_id=self.mount_2)
            ]
        )

    def test_check(self):
        perevals = Perevals.objects.all()
        serializer_data = PerevalsSerializer(perevals, many=True).data

        expected_data = [
            {
                'id': 1,
                'beauty_title': 'beauty_title',
                'title': 'title1',
                'other_titles': 'other_titles1',
                'connect': '',
                'status': 'PN',
                # 'add_time': self.mount_1.add_time.strftime('%Y-%m-%dT%H:%M:%S.$fZ'),
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
                'images': [
                    {
                        'title': 'Title_1',
                        'image': 'https://www.istockphoto.com/ru/фото/перевал-винозе-gm603870390-103682777'
                    },
                    {
                        'title': 'Title_2',
                        'image': 'https://www.istockphoto.com/ru/фото/перевал-харднот-gm603870438-103682825'
                    }
                ]
            },
            {
                'id': 2,
                'beauty_title': 'beauty_title2',
                'title': 'title2',
                'other_titles': 'other_titles2',
                'connect': '',
                'status': 'NW',
                # 'add_time': self.mount_2.add_time.strftime('%Y-%m-%dT%H:%M:%S.$fZ'),
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
                'images': [
                    {
                        'title': 'Title_3',
                        'image': 'https://www.istockphoto.com/ru/фото/камень-пирамида-из-камней-gm471001336-62533536'
                    },
                    {
                        'title': 'Title_4',
                        'image': 'https://www.istockphoto.com/ru/фото/coniston-выполняют-gm471001332-62533240'
                    }
                ]
            }
        ]

        self.assertEqual(serializer_data, expected_data)




