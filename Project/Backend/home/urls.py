from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Route for the home app index view
]

