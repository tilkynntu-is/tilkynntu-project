from django.shortcuts import render, get_object_or_404
from home.models import Report

def view_report(request, report_id=None):
    report = None
    if report_id:
        try:
            report = Report.objects.get(id=report_id)
        except Report.DoesNotExist:
            report = None
    return render(request, 'report_viewer/viewer.html', {'reports': [report] if report else []})
