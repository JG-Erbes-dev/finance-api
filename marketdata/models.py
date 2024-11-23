from django.db import models
from search.models import BrStock as BrStock_S, UsStock as UsStock_S, BrRealEstate as BrRealEstate_S, UsEtf as UsEtf_S, Crypto as Crypto_S, BrTreasure as BrTreasure_S


class BrStock(models.Model):
    ticker = models.ForeignKey(BrStock_S, on_delete=models.PROTECT, db_index=True,
                               related_name='br_stocks', verbose_name='Código')
    date = models.DateField(verbose_name='Data')
    price = models.FloatField(verbose_name='Preço')
    volume = models.FloatField(blank=True, null=True, verbose_name='Volume')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['ticker']
        verbose_name = 'Ações BR'
        verbose_name_plural = 'Ações BR'

    def __str__(self):
        return str(self.ticker)


class UsStock(models.Model):
    ticker = models.ForeignKey(UsStock_S, on_delete=models.PROTECT, db_index=True,
                               related_name='us_stocks', verbose_name='Código')
    date = models.DateField(verbose_name='Data')
    price = models.FloatField(verbose_name='Preço')
    volume = models.FloatField(blank=True, null=True, verbose_name='Volume')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['ticker']
        verbose_name = 'Ações US'
        verbose_name_plural = 'Ações US'

    def __str__(self):
        return str(self.ticker)


class BrRealEstate(models.Model):
    ticker = models.ForeignKey(BrRealEstate_S, on_delete=models.PROTECT, db_index=True,
                               related_name='br_realestates', verbose_name='Código')
    date = models.DateField(verbose_name='Data')
    price = models.FloatField(verbose_name='Preço')
    volume = models.FloatField(blank=True, null=True, verbose_name='Volume')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['ticker']
        verbose_name = 'FIIs'
        verbose_name_plural = 'FIIs'

    def __str__(self):
        return str(self.ticker)


class UsEtf(models.Model):
    ticker = models.ForeignKey(UsEtf_S, on_delete=models.PROTECT, db_index=True,
                               related_name='us_etfs', verbose_name='Código')
    date = models.DateField(verbose_name='Data')
    price = models.FloatField(verbose_name='Preço')
    volume = models.FloatField(blank=True, null=True, verbose_name='Volume')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['ticker']
        verbose_name = 'ETFs US'
        verbose_name_plural = 'ETFs US'

    def __str__(self):
        return str(self.ticker)


class Crypto(models.Model):
    ticker = models.ForeignKey(Crypto_S, on_delete=models.PROTECT, db_index=True,
                               related_name='cryptos', verbose_name='Código')
    date = models.DateField(verbose_name='Data')
    price = models.FloatField(verbose_name='Preço')
    volume = models.FloatField(blank=True, null=True, verbose_name='Volume')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['ticker']
        verbose_name = 'Criptomoedas'
        verbose_name_plural = 'Criptomoedas'

    def __str__(self):
        return str(self.ticker)


class BrTreasure(models.Model):
    title = models.ForeignKey(BrTreasure_S, on_delete=models.PROTECT, db_index=True,
                              related_name='br_treasures', blank=True, null=True, verbose_name='Título')
    date = models.DateField(verbose_name='Data')
    price = models.FloatField(verbose_name='Preço')
    volume = models.FloatField(blank=True, null=True, verbose_name='Volume')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']
        verbose_name = 'Tesouro Direto'
        verbose_name_plural = 'Tesouro Direto'

    def __str__(self):
        return str(self.title)


class Stats(models.Model):
    ticker = models.CharField(max_length=50, blank=True, null=True)
    data_inicio = models.CharField(max_length=10, blank=True, null=True)
    model = models.CharField(max_length=50)

    class Meta:
        ordering = ['model']
        verbose_name = 'Estatística'

    def __str__(self):
        return str(self.ticker)