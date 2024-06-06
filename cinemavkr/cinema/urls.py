from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,), # Главная страница
    path("today", views.today, name = 'today'), #Страница с фильмами, которые можно посмотреть сейчас(бронирование, информация о фильме)
    path("soon", views.soon, name = 'soon'), # Страница с будущими фильмами(информация о фильме)
    path("contacts", views.contacts, name = 'contacts'), # Страница с информацией о кинотеатре(телефоны, адрес и т.д)
    path("news", views.news, name = 'news'),
    path("today/<int:pk>", views.MoviesDetailView.as_view(), name = 'movie_detail'),
    path('booking/<int:pk>/', views.BookingView.as_view(), name='booking'),
    path('book_seat/', views.book_seat, name='book_seat'),
]
