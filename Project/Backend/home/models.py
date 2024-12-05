import uuid
from datetime import datetime
from django.db import models


class User(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    username = models.CharField(max_length=256),
    email = models.EmailField(max_length=254),
    time_joined = models.DateTimeField(
        "time joined", default=datetime.now),


class Tag(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    text = models.CharField(max_length=64, unique=True),


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    time_uploaded = models.DateTimeField(
        "time uploaded", default=datetime.now),
    url = models.URLField(max_length=1024),
    alt_text = models.TextField(),


class Report(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    user_id = models.ForeignKey(User, on_delete=models.CASCADE),
    time_published = models.DateTimeField(
        "time published", default=datetime.now),
    loc_lat = models.DecimalField(max_digits=9, decimal_places=6),
    loc_lng = models.DecimalField(max_digits=9, decimal_places=6),
    title = models.CharField(max_length=64),
    description = models.TextField(),
    tags = models.ManyToManyField(Tag),
    image = models.ForeignKey(Image, on_delete=models.CASCADE),


class Rating(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING),
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING),
    is_positive = models.BooleanField(),
    time_rated = models.DateTimeField("time rated", default=datetime.now),


class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING),
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING),
    time_posted = models.DateTimeField("time posted", default=datetime.now),
    text = models.CharField(max_length=256),
