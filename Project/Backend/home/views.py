from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request: HttpRequest) -> HttpResponse: #{
    template = loader.get_template("home/index.html")
    context = {}

    return HttpResponse(template.render(context, request))
#}
