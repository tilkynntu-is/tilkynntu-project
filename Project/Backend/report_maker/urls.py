from django.urls import URLPattern, path

from . import views

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
    path("/htmx_accept_popup",
         views.htmx_accept_popup, name="htmx_accept_popup"),
]
