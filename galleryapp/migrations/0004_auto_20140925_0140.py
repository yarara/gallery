# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0003_auto_20140923_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.OneToOneField(verbose_name='user', related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]
