# Generated by Django 5.1.1 on 2024-11-01 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0003_remove_brrealestate_industry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brrealestate',
            name='name',
        ),
        migrations.RemoveField(
            model_name='brstock',
            name='name',
        ),
        migrations.RemoveField(
            model_name='crypto',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usetf',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usstock',
            name='name',
        ),
    ]
