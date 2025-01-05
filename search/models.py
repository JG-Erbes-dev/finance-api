from django.db import models


"""
Models de armazenamento de dados básicos dos ativos.

Este módulo contém as classes que representam os ativos disponíveis no sistema, incluindo:
  - Ações brasileiras (BR Stock)
  - Ações americanas (US Stock)
  - FIIs brasileiros (BR Real Estate)
  - ETFs americanos (US ETF)
  - Criptomoedas (Crypto)
  - Títulos do Tesouro Direto brasileiro (BR Treasure)

Finalidade:
  - Utilizado para buscas internas do sistema e da API.
  - Facilita as integrações da API com fontes de dados externas (APIs e sites).
"""

class BrStock(models.Model):
    """
    Classe de dados básicos de ações brasileiras.
    """
    ticker = models.CharField(max_length=30, db_index=True, verbose_name='Código')
    name = models.CharField(max_length=200, verbose_name='Nome')
    sector = models.CharField(max_length=200, verbose_name='Setor')
    industry = models.CharField(max_length=200, verbose_name='Indústria')
    segment = models.CharField(max_length=200, blank=True, null=True, verbose_name='Segmento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Ações BR'
        verbose_name_plural = 'Ações BR'

    def __str__(self):
        return str(self.ticker)


class UsStock(models.Model):
    """
    Classe de dados básicos de ações americanas.
    """
    ticker = models.CharField(max_length=30, db_index=True, verbose_name='Código')
    name = models.CharField(max_length=200, verbose_name='Nome')
    sector = models.CharField(max_length=200, verbose_name='Setor')
    industry = models.CharField(max_length=200, verbose_name='Indústria')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Ações US'
        verbose_name_plural = 'Ações US'

    def __str__(self):
        return str(self.ticker)


class BrRealEstate(models.Model):
    """
    Classe de dados básicos de FIIs brasileiros.
    """
    ticker = models.CharField(max_length=30, db_index=True, verbose_name='Código')
    name = models.CharField(max_length=200, verbose_name='Nome')
    type = models.CharField(max_length=200, verbose_name='Tipo')
    segment = models.CharField(max_length=200, verbose_name='Segmento')
    management = models.CharField(max_length=200, verbose_name='Gestão')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'FIIs'
        verbose_name_plural = 'FIIs'

    def __str__(self):
        return str(self.ticker)


class UsEtf(models.Model):
    """
    Classe de dados básicos de ETFs americanos.
    """
    ticker = models.CharField(max_length=30, db_index=True, verbose_name='Código')
    name = models.CharField(max_length=200, verbose_name='Nome')
    category = models.CharField(max_length=200, verbose_name='Categoria')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'ETFs US'
        verbose_name_plural = 'ETFs US'

    def __str__(self):
        return str(self.ticker)


class Crypto(models.Model):
    """
    Classe de dados básicos de criptomoedas.
    """
    ticker = models.CharField(max_length=30, db_index=True, verbose_name='Código')
    name = models.CharField(max_length=100, verbose_name='Nome')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Criptomoedas'
        verbose_name_plural = 'Criptomoedas'

    def __str__(self):
        return str(self.ticker)


class BrTreasure(models.Model):
    """
    Classe de dados básicos de títulos do tesouro direto brasileiro.
    """
    title = models.CharField(max_length=200, db_index=True, unique=True, blank=True, verbose_name='Título')
    title_type = models.CharField(max_length=200, verbose_name='Tipo de Título')
    maturity = models.DateField(verbose_name='Vencimento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Tesouro Direto'
        verbose_name_plural = 'Tesouro Direto'

    def __str__(self):
        return str(self.title)
