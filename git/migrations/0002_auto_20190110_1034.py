# Generated by Django 2.1.4 on 2019-01-10 07:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('git', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='usern',
        ),
        migrations.AddField(
            model_name='repository',
            name='usern',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
