# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150409_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='pure_html',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
