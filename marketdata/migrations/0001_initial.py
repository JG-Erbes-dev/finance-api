# Generated by Django 5.1.1 on 2024-11-01 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrRealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_realestate_industries', to='search.brrealestate')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_ealestate_names', to='search.brrealestate')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_realestate_sectors', to='search.brrealestate')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_realestates', to='search.brrealestate')),
            ],
        ),
        migrations.CreateModel(
            name='BrStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_stock_industries', to='search.brstock')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_stock_names', to='search.brstock')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_stock_sectors', to='search.brstock')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_stocks', to='search.brstock')),
            ],
        ),
        migrations.CreateModel(
            name='BrTreasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profitability', models.FloatField()),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maturity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_treasure_maturities', to='search.brtreasure')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='br_treasures', to='search.brtreasure')),
            ],
        ),
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='crypto_names', to='search.crypto')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cryptos', to='search.crypto')),
            ],
        ),
        migrations.CreateModel(
            name='UsEtf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_etf_industries', to='search.usetf')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_etf_names', to='search.usetf')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_etf_sectors', to='search.usetf')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_etfs', to='search.usetf')),
            ],
        ),
        migrations.CreateModel(
            name='UsStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_stock_industries', to='search.usstock')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_stock_names', to='search.usstock')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_stock_sectors', to='search.usstock')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='us_stocks', to='search.usstock')),
            ],
        ),
    ]
