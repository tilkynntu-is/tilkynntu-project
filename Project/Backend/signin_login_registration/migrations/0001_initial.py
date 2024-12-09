from home.models import Tag, Image, Report, Rating, Comment
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency('auth.User'),  # this has Dependency on the built-in User model
    ]

    operations = [
        # reminder No `CreateModel` operations are needed here because the models are already defined in `home.models`.
        # reminder This migration simply ensures the `signin_login_registration` app is initialized without duplicating tables.
    ]
