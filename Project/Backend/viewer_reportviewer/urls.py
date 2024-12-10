from django.urls import path
from . import views

urlpatterns = [
    path('viewer/', views.viewer_page, name='viewer'),
]
