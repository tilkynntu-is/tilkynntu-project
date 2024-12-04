from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewer, name='signin'),  # Connects /viewer/ to the viewer view
]
