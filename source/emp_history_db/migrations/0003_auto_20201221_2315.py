# Generated by Django 3.1.3 on 2020-12-21 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_history_db', '0002_auto_20201221_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapointsetpoint',
            old_name='schedule',
            new_name='setpoint',
        ),
    ]
