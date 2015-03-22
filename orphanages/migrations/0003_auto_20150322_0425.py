# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanages', '0002_orphanage_no_of_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oldagehome',
            fields=[
                ('olid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=1000)),
                ('contact_number', models.CharField(max_length=35)),
                ('description', models.TextField(max_length=4000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orphanage',
            name='description',
            field=models.TextField(default='', max_length=4000),
            preserve_default=False,
        ),
    ]
