from django.urls import path, include  # Import 'path' and 'include'
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Route for the home app index view
]
