from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('script', csrf_exempt(views.ReturnScript.as_view()), name='script'),
    path('log', csrf_exempt(views.Logs.as_view()), name='log'),
]