# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150419_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='alignment',
            field=models.CharField(blank=True, max_length=400, null=True, choices=[(b'L', b'Left'), (b'R', b'Right')]),
            preserve_default=True,
        ),
    ]
