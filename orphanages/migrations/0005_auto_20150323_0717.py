# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanages', '0004_auto_20150322_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birthdaysponsor',
            fields=[
                ('bid', models.AutoField(serialize=False, primary_key=True)),
                ('donators_name', models.CharField(max_length=200)),
                ('birthday_person_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('orphanage', models.ForeignKey(to='orphanages.Orphanage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='oldagehome',
            name='description',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oldagehome',
            name='donation_link',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orphanage',
            name='description',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orphanage',
            name='donation_link',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
