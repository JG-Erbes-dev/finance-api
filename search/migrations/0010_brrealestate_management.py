# Generated by Django 5.1.1 on 2024-11-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_remove_brrealestate_industry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brrealestate',
            name='management',
            field=models.CharField(default=0, max_length=200, verbose_name='Gestão'),
            preserve_default=False,
        ),
    ]
