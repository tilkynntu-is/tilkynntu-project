from django.http import HttpResponse
from django.shortcuts import render
from django.http.request import HttpRequest
from django.template import loader

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("report_maker/index.html")
    context = {
        "x_coord": 64.139251,
        "y_coord": -21.902416,
        "zoom": 15,
    }

    return HttpResponse(template.render(context, request))
