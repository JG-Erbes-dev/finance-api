# Generated by Django 5.1.1 on 2024-11-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_remove_usetf_segment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brrealestate',
            name='ticker',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='brstock',
            name='ticker',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='brtreasure',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=200, unique=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='ticker',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='usetf',
            name='ticker',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='usstock',
            name='ticker',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Código'),
        ),
    ]
