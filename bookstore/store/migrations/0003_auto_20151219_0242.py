# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20151218_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 19, 2, 42, 29, 19862, tzinfo=utc)),
        ),
    ]
