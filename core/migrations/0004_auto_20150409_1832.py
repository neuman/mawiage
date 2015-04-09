# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150409_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='image_file',
            field=models.ImageField(max_length=400, null=True, upload_to=core.models.upload_to_location, blank=True),
            preserve_default=True,
        ),
    ]
