from django.db import models


class BrInterestRate(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Taxa de Juros BR'
        verbose_name_plural = 'Taxa de Juros BR'

    def __str__(self):
        return f"{self.date}: {self.value}"


class UsInterestRate(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Taxa de Juros US'
        verbose_name_plural = 'Taxa de Juros US'

    def __str__(self):
        return f"{self.date}: {self.value}"


class BrCDI(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'CDI'
        verbose_name_plural = 'CDI'

    def __str__(self):
        return f"{self.date}: {self.value}"


class CumulativeBrCDI(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'CDI Acumulado'
        verbose_name_plural = 'CDI Acumulado'

    def __str__(self):
        return f"{self.date}: {self.value}"


class BrInflation(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Inflação BR'
        verbose_name_plural = 'Inflação BR'

    def __str__(self):
        return f"{self.date}: {self.value}"
    
    
class CumulativeBrInflation(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Inflação Acumulada BR'
        verbose_name_plural = 'Inflação Acumulada BR'

    def __str__(self):
        return f"{self.date}: {self.value}"


class UsInflation(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Inflação US'
        verbose_name_plural = 'Inflação US'

    def __str__(self):
        return f"{self.date}: {self.value}"


class DollarExchangeRate(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Dólar'
        verbose_name_plural = 'Dólar'

    def __str__(self):
        return f"{self.date}: {self.value}"


class CommodityPrice(models.Model):
    date = models.DateField(unique=True, verbose_name='Data')
    value = models.FloatField(verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Commodities'
        verbose_name_plural = 'Commodities'

    def __str__(self):
        return f"{self.date}: {self.value}"
