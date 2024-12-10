from django.contrib import admin
from django.urls import path, include
from django.urls import URLPattern, path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("help/", views.help, name="help"),
    path("contact/", views.contact, name="contact"),
    path('admin/', admin.site.urls),
    path('auth/', include('signin_login_registration.urls')),
]
