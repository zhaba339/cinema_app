from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    lead_roles = models.TextField()


class Showtime(models.Model):
    start_datetime = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)


class Hall(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


class Seat(models.Model):
    number = models.PositiveIntegerField()
    status = models.CharField(max_length=20)    # Например: booked, available и т.д.
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE),
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE),
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)