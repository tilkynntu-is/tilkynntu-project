import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User;


class Tag(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return f"id: {self.id}, text: {self.text}"


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    time_uploaded = models.DateTimeField(
        "time uploaded", default=datetime.now)
    url = models.URLField(max_length=1024)
    alt_text = models.TextField()

    def __str__(self) -> str:
        return f"id: {self.id}, time_uploaded: {self.time_uploaded}, url: {self.url}, alt_text: {self.alt_text}"


class Report(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_published = models.DateTimeField(
        "time published", default=datetime.now)
    loc_lat = models.DecimalField(max_digits=9, decimal_places=6)
    loc_lng = models.DecimalField(max_digits=9, decimal_places=6)
    title = models.CharField(max_length=64)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"id; {self.id}, time_published: {self.time_published}, location: ({self.loc_lat}, {self.loc_lng}), title: {self.title}, description: {self.description}, tags: {self.tags.get()}, image: {self.image}"


class Rating(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING)
    is_positive = models.BooleanField()
    time_rated = models.DateTimeField("time rated", default=datetime.now)

    def __str__(self) -> str:
        return f"id: {self.id}, user: {self.user}, report: {self.report}, is_positive: {self.is_positive}, time_rated: {self.time_rated}"


class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING, null=True)
    time_posted = models.DateTimeField("time posted", default=datetime.now)
    text = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"id: {self.id}, user: {self.user}, report: {self.report}, time_posted: {self.time_posted}, text: {self.text}"