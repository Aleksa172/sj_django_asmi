# Generated by Django 3.1.4 on 2020-12-23 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_playeruser_achieved_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playeruser',
            name='achieved_at',
        ),
    ]