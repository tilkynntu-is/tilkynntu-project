from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  
    path('login/', views.login_view, name='login'),  
    path('success/', views.success_view, name='success'),  
    path('logout/', views.logout_view, name='logout'), 
]
