# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_auto_20151219_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('order_date', models.DateField(null=True)),
                ('payment_type', models.CharField(max_length=100, null=True)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 19, 16, 47, 54, 976479, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 19, 16, 47, 54, 977385, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='book',
            field=models.ForeignKey(to='store.Book'),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='cart',
            field=models.ForeignKey(to='store.Cart'),
        ),
    ]
