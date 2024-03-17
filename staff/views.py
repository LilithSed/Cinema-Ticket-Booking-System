from datetime import date, timedelta

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from accounts.models import Account
from accounts.views import staff_required
from booking.models import booking
from .forms import showForm
from .models import film, show, banner


def base(request):
    return render(request, "admin_base.html")


# LOGING VIEWS
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def index(request):
    context = {}
    start_date = date.today() - timedelta(days=2)

    b_data = booking.objects.filter(show_date__gte=start_date).values_list(
        'show_date').order_by('show_date').annotate(total_seats=Sum('num_seats'))
    r_data = booking.objects.filter(show_date__gte=start_date).values_list(
        'show_date').order_by('show_date').annotate(total=Sum('total'))

    booking_table = booking.objects.select_related().order_by('-booked_date').values_list(
        'show_date', 'booked_date', 'show', 'total', 'num_seats',
        'show__movie__movie_name', 'show__showtime',
        named=True
    )
    movies_count = film.objects.all().count()
    users_count = Account.objects.filter(is_staff=False).count()
    bookings_count = booking.objects.all().count()

    days = 7
    date_labels = set(start_date + timedelta(x) for x in range(days))
    date_labels = sorted(date_labels)

    graph1 = {}
    data_dict = {}
    for r in b_data:
        # legend of fields: date 0, no of tickets 1
        data_dict[r[0]] = r[1]
    for d in date_labels:
        if (d not in data_dict.keys()):
            data_dict[d] = 0
    graph1['dates'] = ",".join([x.strftime("%b %d") for x in date_labels])
    graph1['tickets'] = [data_dict[x] for x in date_labels]

    graph2 = {}
    data_dict = {}
    for r in r_data:
        # legend of fields: date 0, no of tickets 1
        data_dict[r[0]] = r[1]
    for d in date_labels:
        if (d not in data_dict.keys()):
            data_dict[d] = 0
    graph2['dates'] = ",".join([x.strftime("%b %d") for x in date_labels])
    graph2['total'] = [data_dict[x] for x in date_labels]

    context = {
        'graph1': graph1,
        'graph2': graph2,
        'tabledata': booking_table,
        'movies_count': movies_count,
        'users_count': users_count,
        'bookings_count': bookings_count
    }

    return render(request, "dashboard.html", context)


# FILM VIEWS
class FilmCreate(CreateView):
    template_name = "film/add_film.html"
    model = film
    fields = ['movie_name', 'url', 'room']
    success_url = reverse_lazy('movies')


class FilmUpdate(UpdateView):
    template_name = "film/edit_film.html"
    model = film
    fields = ['movie_name', 'url', 'room']
    success_url = reverse_lazy('movies')


class FilmDelete(DeleteView):
    template_name = "film/delete_film.html"
    model = film
    success_url = reverse_lazy('movies')


# SHOW VIEWS
class ShowCreate(CreateView):
    template_name = "show/add_show.html"
    form_class: showForm
    model = show
    fields = ['movie', 'start_date', 'end_date', 'price', 'showtime', 'room']
    success_url = reverse_lazy('shows')


class ShowUpdate(UpdateView):
    template_name = "show/edit_show.html"
    form_class: showForm
    model = show
    fields = ['movie', 'start_date', 'end_date', 'price', 'showtime', 'room']
    success_url = reverse_lazy('shows')


class ShowDelete(DeleteView):
    template_name = "show/delete_show.html"
    model = show
    success_url = reverse_lazy('shows')


# MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def movies(request):
    movies = film.objects.filter().order_by('-id').values_list('id',
                                                               'movie_name', 'date_added', 'url', named=True)
    return render(request, "movies.html", {'film_list': movies})


# SHOW VIEWS
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def shows(request):
    shows = show.objects.all().order_by('-id')
    return render(request, "shows.html", context={'shows': shows})
