from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('adminlogin/', views.admin_login, name='admin login'),
    path('logout/', views.signout, name="logout"), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
