# Generated by Django 5.1.1 on 2024-11-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_remove_brrealestate_segment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brrealestate',
            name='sector',
            field=models.CharField(max_length=200, verbose_name='Setor'),
        ),
    ]
