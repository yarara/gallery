# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galleryapp', '0010_auto_20140928_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(null=True, verbose_name='user', default=1, blank=True, to=settings.AUTH_USER_MODEL, related_name='user_id'),
            preserve_default=True,
        ),
    ]
