# Generated by Django 5.1.1 on 2024-11-03 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0004_remove_brrealestate_name_remove_brstock_name_and_more'),
        ('search', '0002_rename_industry_usetf_category_remove_usetf_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brtreasure',
            name='title',
        ),
        migrations.AddField(
            model_name='brtreasure',
            name='title_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='br_treasures_titles', to='search.brtreasure'),
        ),
        migrations.AlterField(
            model_name='brtreasure',
            name='maturity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='br_treasure_maturities', to='search.brtreasure'),
        ),
    ]