from django.db import models
import uuid

# Create your models here.

class ImageContainer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.ImageField(upload_to="uploads/")
