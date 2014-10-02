# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_update',
            field=models.DateTimeField(verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_upload',
            field=models.DateTimeField(verbose_name='Дата загрузки'),
        ),
    ]
