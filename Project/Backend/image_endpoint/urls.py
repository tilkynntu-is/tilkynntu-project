from django.urls import URLPattern, path

from . import views

app_name = "images"
urlpatterns: list[URLPattern] = [
    path("uuid/<str:image_uuid>/", views.get_uuid, name="image_uuid")
]
