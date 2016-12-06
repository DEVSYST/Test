# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medfreq', '0002_auto_20161201_0948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Frequency',
            new_name='IllnessItem',
        ),
    ]
