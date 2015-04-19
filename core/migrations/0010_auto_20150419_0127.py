# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150419_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content_style',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'C', b'HTML Content'), (b'P', b'Pure HTML')]),
            preserve_default=True,
        ),
    ]
