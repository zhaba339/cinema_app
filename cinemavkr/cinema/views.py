from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie, Seat, Showtime, Hall
from django.views.generic import DetailView
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'cinema/index.html')


def today(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/today.html', {'movies': movies})


class MoviesDetailView(DetailView):
    model = Movie
    template_name = 'cinema/movie_detail.html'
    template_name_booking = 'cinema/booking.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        date_str = self.request.GET.get('date')

        if date_str:
            date = parse_date(date_str)
            showtimes = Showtime.objects.filter(movie=movie, start_datetime__date=date)
        else:
            showtimes = []

        context['showtimes'] = showtimes
        context['date_selected'] = bool(date_str)  # Проверка, выбрана ли дата
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            movie = self.get_object()
            date_str = request.GET.get('date')
            if date_str:
                date = parse_date(date_str)
                showtimes = Showtime.objects.filter(movie=movie, start_datetime__date=date)
                sessions = [
                    {
                        'start_datetime': showtime.start_datetime.strftime('%H:%M'),
                        'booking_url': showtime.get_booking_url()
                    }
                    for showtime in showtimes
                ]
            else:
                sessions = []
            return JsonResponse({'sessions': sessions})
        return super().get(request, *args, **kwargs)


def booking(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    hall = get_object_or_404(Hall, movie=movie)
    seats = Seat.objects.filter(hall=hall).order_by('row', 'number')
    if request.method == 'POST':
        seat_ids = request.POST.getlist('seat_ids[]')
        for seat_id in seat_ids:
            seat = Seat.objects.get(pk=seat_id)
            seat.status = 'booked'
            seat.save()
        return JsonResponse({'status': 'success', 'message': 'Seats booked successfully.'})
    return render(request, 'cinema/booking.html', {'movie': movie, 'hall': hall, 'seats': seats})


class BookingView(DetailView):
    model = Hall
    template_name = 'cinema/booking.html'
    context_object_name = 'hall'


@csrf_exempt
def book_seat(request):
    if request.method == 'POST':
        seat_ids = request.POST.getlist('seat_ids[]')
        seats = Seat.objects.filter(id__in=seat_ids)
        for seat in seats:
            seat.status = 'booked'
            seat.save()
        return JsonResponse({'status': 'success', 'message': 'Seats booked successfully.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})


def soon(request):
    return render(request, 'cinema/soon.html')


def contacts(request):
    return render(request, 'cinema/contacts.html')


def news(request):
    return render(request, 'cinema/news.html')


