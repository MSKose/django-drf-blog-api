# Generated by Django 4.1.1 on 2022-10-20 11:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog_view',
        ),
        migrations.AddField(
            model_name='post',
            name='blog_view',
            field=models.ManyToManyField(related_name='collected_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
