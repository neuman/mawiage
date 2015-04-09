# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_chapter_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='location',
            new_name='story',
        ),
    ]
