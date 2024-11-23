# Generated by Django 5.1.1 on 2024-11-06 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0006_rename_title_type_brtreasure_title'),
        ('search', '0002_rename_industry_usetf_category_remove_usetf_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='brtreasure',
            name='title_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='brtreasure',
            name='maturity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brtreasure',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='br_treasures', to='search.brtreasure'),
        ),
    ]