from django.urls import path
from .views import landing
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("thank-you/", views.thank_you, name="thank_you"),
]