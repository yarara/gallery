# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', default='', verbose_name='Изображение')),
                ('date_upload', models.DateField()),
                ('date_update', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text_note', models.TextField(default='', blank=True, verbose_name='Изображение')),
                ('image_id', models.ForeignKey(to='galleryapp.Image', verbose_name='Изображение')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
