# Generated by Django 5.1.1 on 2024-11-01 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0001_initial'),
        ('search', '0002_rename_industry_usetf_category_remove_usetf_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usetf',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='usetf',
            name='sector',
        ),
        migrations.AddField(
            model_name='usetf',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='us_etf_categories', to='search.usetf'),
            preserve_default=False,
        ),
    ]
