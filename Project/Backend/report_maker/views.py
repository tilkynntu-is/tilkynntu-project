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


def htmx_accept_popup(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("report_maker/accept_popup.html")
    context = {
        "popup_title": "accept",
        "popup_text": "is this right?",
        "button_1_text": "Decline",
        "button_2_text": "Accept",
    }

    return HttpResponse(template.render(context, request))


def htmx_get_tag(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("report_maker/tag.html")
    context = {
        "tag_text": request.GET.get("tag_text"),
    }
    return HttpResponse(template.render(context, request))
