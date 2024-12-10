from django.contrib.auth.models import AnonymousUser, User
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.template import loader
from home.models import Report, Tag, Rating, Comment, Image
from image_endpoint.models import ImageContainer
import json

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


def upload(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        request_dict: dict = json.loads(str(request.POST.get("json")))
        print(request_dict)
        title: str = request_dict["title"]
        description: str = request_dict["description"]
        tag_list: list[Tag] = [Tag.objects.get_or_create(
            text=tag)[0] for tag in request_dict["tag_list"]]
        loc_lat: float = request_dict["location"]["lat"]
        loc_lng: float = request_dict["location"]["lng"]

        if isinstance(request.FILES["image"], UploadedFile):
            image_file = request.FILES["image"]
        else:
            return HttpResponseBadRequest()
        image = Image()
        image.create_image(image=image_file, alt_text="")
        image.save()

        user = request.user if request.user.is_authenticated else User.objects.get_or_create(
            username="guest", email="guest@example.org")

        report = Report(user_id=user, loc_lat=loc_lat, loc_lng=loc_lng,
                        title=title, description=description, image=image)
        report.save()
        report.tags.set(tag_list)

        return redirect(f"/tilkynningar/#report-{report.id}")
    else:
        return HttpResponseForbidden()
