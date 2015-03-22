# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('orid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=1000)),
                ('contact_number', models.CharField(max_length=35)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
