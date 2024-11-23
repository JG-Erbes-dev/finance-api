from django.db import models
from search.models import BrStock as BrStock_S, UsStock as UsStock_S, BrRealEstate as BrRealEstate_S, UsEtf as UsEtf_S


class BrStock(models.Model):
    ticker = models.ForeignKey(BrStock_S, on_delete=models.PROTECT, db_index=True,
                               related_name='events_br_stocks', verbose_name='Código')
    event_date = models.DateField(verbose_name='Data')
    event_type = models.CharField(max_length=200, verbose_name='Evento')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Ações BR'
        verbose_name_plural = 'Ações BR'

    def __str__(self):
        return str(self.ticker)


class UsStock(models.Model):
    ticker = models.ForeignKey(UsStock_S, on_delete=models.PROTECT, db_index=True,
                               related_name='events_us_stocks', verbose_name='Código')
    event_date = models.DateField(verbose_name='Data')
    event_type = models.CharField(max_length=200, verbose_name='Evento')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Ações US'
        verbose_name_plural = 'Ações US'

    def __str__(self):
        return str(self.ticker)
    

class BrRealEstate(models.Model):
    ticker = models.ForeignKey(BrRealEstate_S, on_delete=models.PROTECT, db_index=True,
                               related_name='events_br_realestates', verbose_name='Código')
    event_date = models.DateField(verbose_name='Data')
    event_type = models.CharField(max_length=200, verbose_name='Evento')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'FIIs'
        verbose_name_plural = 'FIIs'

    def __str__(self):
        return str(self.ticker)
    
    
class UsEtf(models.Model):
    ticker = models.ForeignKey(UsEtf_S, on_delete=models.PROTECT, db_index=True,
                               related_name='events_us_etfs', verbose_name='Código')
    event_date = models.DateField(verbose_name='Data')
    event_type = models.CharField(max_length=200, verbose_name='Evento')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'ETFs US'
        verbose_name_plural = 'ETFs US'

    def __str__(self):
        return str(self.ticker)
