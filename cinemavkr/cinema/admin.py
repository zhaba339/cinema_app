from django.contrib import admin

from .models import Movie, Showtime, Hall, User, Seat, Reservation

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Hall)
admin.site.register(User)
admin.site.register(Seat)
admin.site.register(Reservation)
