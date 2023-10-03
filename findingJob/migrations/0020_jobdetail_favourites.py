# Generated by Django 3.2.12 on 2022-04-25 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('findingJob', '0019_auto_20220422_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetail',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favouritte', to=settings.AUTH_USER_MODEL),
        ),
    ]