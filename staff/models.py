from django.db import models
from django.utils import timezone


class Film(models.Model):
    ROOM_CHOICES = (
        (1, "Blue"),
        (2, "Red"),
        (3, "Green")
    )
    movie_name = models.CharField(verbose_name="Movie Name", max_length=100)
    room = models.IntegerField(
        verbose_name="Room", choices=ROOM_CHOICES, blank=False, null=False, default=1)
    url = models.URLField(verbose_name="Poster", blank=True, null=True)
    date_added = models.DateField(
        auto_now=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.movie_name


class Banner(models.Model):
    movie = models.ForeignKey(
        Film, verbose_name="Movie", on_delete=models.CASCADE, blank=True, null=True)
    url = models.URLField(verbose_name="Banner Image URL",
                          blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.movie.movie_name


class Show(models.Model):
    ROOM_CHOICES = (
        (1, "Blue"),
        (2, "Red"),
        (3, "Green")
    )
    movie = models.ForeignKey(
        Film, verbose_name="Movie", on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(verbose_name="Start Date", null=True)
    end_date = models.DateField(verbose_name="End Date", null=True)
    price = models.PositiveIntegerField(verbose_name="Ticket Price")
    showtime = models.TimeField(verbose_name="Showtime", auto_now=False,
                                auto_now_add=False, blank=False, null=False, default=timezone.now)
    room = models.IntegerField(
        verbose_name="Room", choices=ROOM_CHOICES, blank=False, null=False, default=1)
 
 
    def __str__(self):
        return self.movie.movie_name + "@" + self.showtime.strftime("%I:%M %p")
