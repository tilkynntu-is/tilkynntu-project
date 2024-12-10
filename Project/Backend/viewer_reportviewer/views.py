from django.shortcuts import render
from .models import Report

def viewer_page(request):
    reports = Report.objects.prefetch_related('tags', 'image').all()
    context = {
        'reports': reports, 
    }
    return render(request, 'viewer.html', context)
