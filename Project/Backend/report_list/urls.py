from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path("", views.index, name="tilkynningar"),
    path("htmx-report/<str:report_id>", views.htmx_report, name="htmx-report"),
    path("htmx-image/<str:image_id>", views.htmx_image, name="htmx-image"),
]
