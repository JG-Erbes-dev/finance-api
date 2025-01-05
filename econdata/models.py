from django.db import models


"""
Models de armazenamento de dados históricos de indicadores econômicos relevantes.

Este módulo contém as classes que armazenam os dados históricos dos indicadores:
  - Taxa de juros brasileira (BR Interest Rate)
  - Taxa de juros americana (US Interest Rate)
  - CDI brasileiro (BR CDI)
  - CDI brasileiro acumulado (Cumulative BR CDI)
  - Inflação brasileira (BR Inflation)
  - Inflação brasileira acumulada (Cumulative BR Inflation)
  - Inflação americana (US Inflation)
  - Taxa de Câmbio Dólar/Real (Dollar Exchange Rate)
  - Preço do Índice de Commoditie Amplo (GD=P) (Commodity Price)

Finalidade:
  - Manter o histórico para uso em análises de cenário e sazonalidade.
  - Utilizar em comparações e estudos históricos de desempenho.
  - Possibilidade de criação de um índice geral de mercado.
"""

class BrInterestRate(models.Model):
    """
    Classe de dados históricos da taxa de juros brasileira.
    """
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
    """
    Classe de dados históricos da taxa de juros americana.
    """
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
    """
    Classe de dados históricos do CDI brasileiro.
    """
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
    """
    Classe de dados históricos acumulados do CDI brasileiro.
    """
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
    """
    Classe de dados históricos da inflação brasileira.
    """
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
    """
    Classe de dados históricos da inflação brasileira acumulada.
    """
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
    """
    Classe de dados históricos da inflação americana.
    """
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
    """
    Classe de dados históricos da taxa de juros dólar/real.
    """
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
    """
    Classe de dados históricos do índice de commoditie amplo GD=P.
    """
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
