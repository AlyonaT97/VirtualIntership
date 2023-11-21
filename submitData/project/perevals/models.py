from django.db import models
from django.core.cache import cache


class Users(models.Model):
    email = models.CharField(max_length=128, unique=True)
    full_name = models.CharField(max_length=128)
    phone = models.IntegerField(unique=True)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Perevals(models.Model):
    new = 'NW'
    pending = 'PN'
    accepted = 'AC'
    rejected = 'RJ'

    CHOICES = [
        (new, 'Новый'),
        (pending, 'Взято в работу'),
        (accepted, 'Успешно'),
        (rejected, 'Отклонено')
    ]

    beautyTitle = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    other_titles = models.CharField(max_length=200)
    connect = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=CHOICES, default=new)
    add_time = models.DateTimeField(auto_now_add=True)
    winter_level = models.CharField(max_length=10)
    summer_level = models.CharField(max_length=10)
    autumn_level = models.CharField(max_length=10)
    spring_level = models.CharField(max_length=10)

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)


class PerevalAreas(models.Model):
    id_parent = models.IntegerField()
    title = models.CharField(max_length=128)


class Images(models.Model):
    title = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    pereval_id = models.ForeignKey(Perevals, on_delete=models.CASCADE)


class PerevalImages(models.Model):
    pereval_id = models.ForeignKey(Perevals, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'image-{self.pk}')


class SprActivitiesTypes(models.Model):
    title = models.CharField(max_length=128)