# Generated by Django 3.1.3 on 2020-12-18 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp_main', '0002_auto_20201014_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatapointValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, default=None, help_text='The value field in datapoint value msg.', null=True)),
                ('timestamp', models.DateTimeField(blank=True, default=None, help_text='The timestamp field in datapoint value msg.', null=True)),
                ('datapoint', models.ForeignKey(help_text='The datapoint that the value message belongs to.', on_delete=django.db.models.deletion.CASCADE, to='emp_main.datapoint')),
            ],
        ),
    ]
