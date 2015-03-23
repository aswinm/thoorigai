# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanages', '0005_auto_20150323_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthdaysponsor',
            name='birthday_person_email',
            field=models.EmailField(default='', max_length=75),
            preserve_default=False,
        ),
    ]
