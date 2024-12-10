from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_report, name='default_view_report'),  # Default route fyrir ekkert id 
    path('<str:report_id>/', views.view_report, name='view_report'),  # Route með report id
]
