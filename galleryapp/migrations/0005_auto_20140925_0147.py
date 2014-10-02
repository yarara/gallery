# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0004_auto_20140925_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_update',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_upload',
            field=models.DateField(null=True, auto_now_add=True, verbose_name='Дата загрузки'),
        ),
    ]
