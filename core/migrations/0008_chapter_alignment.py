# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150410_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='alignment',
            field=models.IntegerField(blank=True, null=True, choices=[(b'L', b'Left'), (b'R', b'Right')]),
            preserve_default=True,
        ),
    ]
