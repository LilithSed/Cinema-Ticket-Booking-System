from datetime import date, datetime, timezone

from django.http import HttpResponse
from django.shortcuts import render

from staff.models import *
from .models import *


def home(request):
    movies = film.objects.filter().values_list(
        'id', 'movie_name', 'url', "room", named=True)
    banners = banner.objects.filter().select_related().values_list(
        'movie__id', 'movie__movie_name', 'url', named=True)
    return render(request, "index.html", context={'films': movies, 'banners': banners})


def movie_detail(request, id):
    context = {}
    context['film'] = film.objects.get(id=id)
    context['showtimes'] = show.objects.filter(movie=id, end_date__gte=date.today(
    )).all().values_list('id', 'showtime', named=True)
    return render(request, "movie_detail.html", context)


def show_select(request):
    if (request.method == "GET" and len(request.GET) != 0):
        date = request.GET['date']
        room = request.GET['room']

        # add showitme >= current time + 5 min
        shows = show.objects.filter(end_date__gte=date, start_date__lte=date).select_related(
            'movie_id', 'movie__url', 'movie__movie_name', 'movie__room').order_by(
            'movie_id', 'showtime').values_list(
                'id', 'price', 'showtime', 'movie', 'movie__url',
                'movie__movie_name', "movie__room",
            named=True
        )
        res_dict = {}

        # Grouping shows rows by movie and appending showitmes in a list
        for s in shows:
            if not str(s[6]) == str(room):
                continue
            # legend of fields: showid 0, price 1, showtime 2, movieid 3, movieurl 4, moviename 5,
            if (s[5] not in res_dict.keys()):
                # movie doesn't exit in dict
                res_dict[s[5]] = {'url': s[4], 'price': s[1], 'room': s[6],
                                  'showtimes': {s[0]: s[2]}, 'movieid': s[3]}
            else:
                # movie already exists
                res_dict[s[5]]['showtimes'][s[0]] = s[2]

    return render(request, "show_selection.html", context={'films': res_dict, 'date': date, 'shows': shows})


def bookedseats(request):
    if request.method == 'GET':
        show_id = request.GET['show_id']
        show_date = request.GET['show_date']
        seats = booking.objects.filter(
            show=show_id, show_date=show_date).values('seat_num')
        booked = ""
        for s in seats:
            booked += s['seat_num']+","
        return HttpResponse(booked[:-1])
    else:
        return HttpResponse("Request method is not a GET")


def checkout(request):
    context = {}
    if (request.method == "POST"):
        show_date = request.POST['showdate']
        seats = request.POST['seats']
        show_id = request.POST['showid']

        # Get Show id
        showinfo = show.objects.get(id=show_id)
        num_seats = len(seats.split(","))
        showinfo = show.objects.get(id=show_id)
        total = showinfo.price*num_seats
        booking.objects.create(booking_code="Random", show=showinfo, show_date=show_date,
                               booked_date=datetime.now(timezone.utc), seat_num=seats, num_seats=num_seats, total=total)

        context["film"] = film.objects.get(movie_name=showinfo.movie)
        context['sdate'] = show_date
        context['seats'] = seats
        context['show'] = showinfo

    return render(request, "checkout.html", context)
