# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_chapter_alignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='pure_html',
        ),
        migrations.AddField(
            model_name='chapter',
            name='content_style',
            field=models.IntegerField(blank=True, null=True, choices=[(b'C', b'HTML Content'), (b'P', b'Pure HTML')]),
            preserve_default=True,
        ),
    ]
