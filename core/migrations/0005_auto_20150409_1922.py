# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150409_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='image_file',
            field=models.ImageField(max_length=400, upload_to=core.models.upload_to_location),
            preserve_default=True,
        ),
    ]
