# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_name', models.CharField(max_length=64, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('User_Barrage', models.TextField(max_length=1024, verbose_name=b'\xe5\xbc\xb9\xe5\xb9\x95\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'db_table': 'Barrage',
                'verbose_name': '\u5f39\u5e55\u8868',
                'verbose_name_plural': '\u5f39\u5e55\u8868',
            },
        ),
    ]
