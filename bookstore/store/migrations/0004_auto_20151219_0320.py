# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20151219_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 19, 3, 20, 42, 201071, tzinfo=utc)),
        ),
    ]
