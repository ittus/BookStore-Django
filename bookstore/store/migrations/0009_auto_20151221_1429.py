# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20151219_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='books/empty_cover.jpg', upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 21, 14, 29, 54, 969420, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 21, 14, 29, 54, 970726, tzinfo=utc)),
        ),
    ]
