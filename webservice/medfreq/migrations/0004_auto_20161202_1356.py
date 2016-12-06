# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medfreq', '0003_auto_20161202_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='illnessitem',
            old_name='fill_time',
            new_name='duty_cycle',
        ),
    ]
