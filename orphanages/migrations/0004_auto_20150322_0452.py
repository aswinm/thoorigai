# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanages', '0003_auto_20150322_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldagehome',
            name='donation_link',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orphanage',
            name='donation_link',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
