# Generated by Django 5.1.1 on 2024-11-10 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_brrealestate_management'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usstock',
            name='segment',
        ),
    ]