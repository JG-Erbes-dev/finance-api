# Generated by Django 5.1.1 on 2024-11-06 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('econdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptodata',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cryptodata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='cryptodata',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='cryptodata',
            name='value',
        ),
    ]
