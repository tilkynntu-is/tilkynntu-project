from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from home.models import *

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("report_list/index.html")
    report_list = map(lambda x:x.id ,list(Report.objects.all()))
    context: dict = {
        "report_list": report_list,
    }
    return HttpResponse(template.render(context, request))

def htmx_report(request: HttpRequest, report_id: str) -> HttpResponse:
    template = loader.get_template("report_list/htmx_report.html")
    report: Report = Report.objects.get(pk=report_id)
    likes: int = Rating.objects.filter(report__id=report.id, is_positive=True).count()
    dislikes: int = Rating.objects.filter(report__id=report.id, is_positive=False).count()
    context: dict = {
        "id": report.id,
        "title": report.title,
        "description": report.description,
        "tags": list(report.tags.all()),
        "location": {"lat": report.loc_lat, "lng": report.loc_lng},
        "time_published": report.time_published,
        "image_id": report.image.id,
        "likes": likes,
        "dislikes": dislikes,
    }
    return HttpResponse(template.render(context, request))

def htmx_image(request: HttpRequest, image_id: str) -> HttpResponse:
    template = loader.get_template("image.html")
    image = Image.objects.get(pk=image_id)
    base_url = str(request.scheme) + '://' + request.get_host() + '/'
    url = base_url+image.path
    context: dict = {
        "id": image.id,
        "alt_text": image.alt_text,
        "url": url,
    }
    return HttpResponse(template.render(context, request))
