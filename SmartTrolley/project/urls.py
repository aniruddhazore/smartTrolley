from django.urls import path
from . import views

from SmartTrolley import settings
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static

app_name = "project"
urlpatterns = [
    path('', csrf_exempt(views.index), name='index'),
]