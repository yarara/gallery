# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0009_auto_20140928_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='account', verbose_name='user', blank=True),
        ),
    ]
