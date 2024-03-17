from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'), 

    # CRUD For Movies
    path('movies', views.movies, name='movies'),
    path('createfilm', views.FilmCreate.as_view(), name='film-create'),
    path('updatefilm/<pk>', views.FilmUpdate.as_view(), name='film-update'),
    path('deletefilm/<pk>', views.FilmDelete.as_view(), name='film-delete'),

    # CRUD For Shows
    path('shows', views.shows, name='shows'),
    path('createshow', views.ShowCreate.as_view(), name='show-create'),
    path('updateshow/<pk>', views.ShowUpdate.as_view(), name='show-update'),
    path('deleteshow/<pk>', views.ShowDelete.as_view(), name='show-delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)