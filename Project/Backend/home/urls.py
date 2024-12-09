from django.contrib import admin
from django.urls import path, include  
from django.urls import URLPattern, path


from . import views

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
        path('admin/', admin.site.urls),
    path('auth/', include('signin_login_registration.urls')), 
]




