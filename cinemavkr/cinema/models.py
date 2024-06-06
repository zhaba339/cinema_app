from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    year = models.PositiveIntegerField(verbose_name='Год')
    duration = models.PositiveIntegerField(verbose_name='Хронометраж')
    country = models.CharField(max_length=255, verbose_name='Страна')
    genre = models.CharField(max_length=255, verbose_name='Жанр')
    director = models.CharField(max_length=255, verbose_name='Режиссер')
    lead_roles = models.TextField(verbose_name='В ролях')
    poster = models.ImageField(upload_to='posters', blank=True, verbose_name='Постер')

    class Meta:
        verbose_name: str = 'Фильм'
        verbose_name_plural: str = 'Фильмы'


class Showtime(models.Model):
    start_datetime = models.DateTimeField(verbose_name='Дата и время начала')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name='Фильм')
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал')

    class Meta:
        verbose_name: str = 'Сеанс'
        verbose_name_plural: str = 'Сеансы'

    def get_booking_url(self):
        return reverse('booking', args=[self.pk])


class Hall(models.Model):
    name = models.CharField(max_length=255, verbose_name='Номер зала')
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')

    class Meta:
        verbose_name: str = 'Зал'
        verbose_name_plural: str = 'Залы'

    def save(self, *args, **kwargs):
        # Проверяем, сохраняется ли новый зал (при создании)
        is_new_hall = not self.pk
        super().save(*args, **kwargs)
        # Если зал новый, создаем для него места
        if is_new_hall:
            self.create_seats()

    def create_seats(self):
        # Создаем места для зала
        for row in range(1, (self.capacity // 5) + 1):  # Вычисляем количество рядов
            for number in range(1, 6):  # В каждом ряду 5 мест
                Seat.objects.create(hall=self, number=number, row=row)
                                                                                                                                            

class Seat(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('booked', 'Booked'),
    ]
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.IntegerField()
    number = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free')

    def __str__(self):
        return f"Ряд {self.row}, место {self.number}"

    class Meta:
        verbose_name: str = 'Место'
        verbose_name_plural: str = 'Места в зале'


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='Юзернейм')
    email = models.EmailField(unique=True, verbose_name='Почта')
    password = models.CharField(max_length=128, verbose_name='Пароль')

    class Meta:
        verbose_name: str = 'Клиент'
        verbose_name_plural: str = 'Клиенты'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE),
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE),
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)

    class Meta:
        verbose_name: str = 'Бронь'
        verbose_name_plural: str = 'Брони'


