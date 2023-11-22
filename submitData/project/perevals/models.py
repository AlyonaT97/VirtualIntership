from django.db import models
from django.core.cache import cache


class Users(models.Model):
    email = models.CharField(max_length=128, unique=True)
    full_name = models.CharField(max_length=128, verbose_name='Полное имя')
    phone = models.IntegerField(unique=True, verbose_name='Телефон')


class Coords(models.Model):
    latitude = models.FloatField(max_length=20, verbose_name='Широта')
    longitude = models.FloatField(max_length=20, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def str(self):
        return f'Широта - {self.latitude}, долгота - {self.longitude}, высота - {self.height}'


class Level(models.Model):
    winter = models.CharField(max_length=2, verbose_name='Зима')
    summer = models.CharField(max_length=2, verbose_name='Лето')
    autumn = models.CharField(max_length=2, verbose_name='Осень')
    spring = models.CharField(max_length=2, verbose_name='Весна')

    def str(self):
        return f'Уровень сложности перевала в зимнее время - {self.winter}, в летнее - {self.summer}, ' \
               f'в осеннее - {self.autumn}, в весеннее - {self.spring}'


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

    beautyTitle = models.CharField(max_length=200, verbose_name='Общее название')
    title = models.CharField(max_length=200, verbose_name='Название перевала')
    other_titles = models.CharField(max_length=200)
    connect = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=CHOICES, default=new)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    level_id = models.ForeignKey(Level, on_delete=models.CASCADE, default=Level.summer)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)

    def str(self):
        return f'Это перевал №{self.pk} под названием "{self.beautyTitle}"'


class PerevalAreas(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название горы')


class Images(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название изображения')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    image = models.ImageField(verbose_name='Изображение', upload_to='images')

    pereval_id = models.ForeignKey(Perevals, on_delete=models.CASCADE)


class PerevalImages(models.Model):
    pereval_id = models.ForeignKey(Perevals, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'image-{self.pk}')


class SprActivitiesTypes(models.Model):
    title = models.CharField(max_length=128, verbose_name='Способ передвижения')
