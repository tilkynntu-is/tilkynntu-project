from django.http import HttpRequest, HttpResponse
from .models import ImageContainer

# Create your views here.

def get_uuid(request: HttpRequest, image_uuid: str) -> HttpResponse:
    image_path = ImageContainer.objects.get(pk=image_uuid).image.path
    with open(image_path, "rb") as image_file:
        return HttpResponse(image_file.read(), content_type="image/jpeg")
