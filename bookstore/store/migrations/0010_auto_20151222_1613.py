# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20151221_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='latitude',
            field=models.FloatField(max_length=20, default='37.4192'),
        ),
        migrations.AddField(
            model_name='review',
            name='longitude',
            field=models.FloatField(max_length=20, default='122.0574'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to=store.models.cover_upload_path, default='books/empty_cover.jpg'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 22, 16, 13, 53, 692292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 22, 16, 13, 53, 694171, tzinfo=utc)),
        ),
    ]
