from django.urls import path
from . import views


urlpatterns = [
    path("", views.index), # Главная страница
    path("films/", views.films), #Страница с фильмами, которые можно посмотреть сейчас(бронирование, информация о фильме)
    path("soon/", views.soon), # Страница с будущими фильмами(информация о фильме)
    path("contacts/", views.contacts), # Страница с информацией о кинотеатре(телефоны, адрес и т.д)
]