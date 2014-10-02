# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0002_auto_20140923_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_update',
            field=models.DateField(verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_upload',
            field=models.DateField(verbose_name='Дата загрузки'),
        ),
    ]
