from django.db import models

from staff.models import show


class booking(models.Model):
    booking_code = models.CharField(max_length=100)
    show = models.ForeignKey(show, on_delete=models.CASCADE)
    seat_num = models.CharField(max_length=25)
    num_seats = models.PositiveSmallIntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    show_date = models.DateField(null=True)
    booked_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)

    def __str__(self) -> str:
        return self.seat_num + "@" + self.show_date.strftime("%m/%d/%Y") + " " + self.show.movie.movie_name
