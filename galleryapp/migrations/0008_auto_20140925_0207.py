# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0007_auto_20140925_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_update',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_upload',
            field=models.DateField(verbose_name='Дата загрузки', auto_now_add=True),
        ),
    ]
