from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='mainpage'), 
    path('detail/<id>', views.movie_detail, name="movie detail"), 
    path('show', views.show_select, name="show select"),
    path('bookedseats', views.bookedseats, name="bookedseats"),
    path('checkout', views.checkout, name="checkout"), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)