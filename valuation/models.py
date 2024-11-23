# from django.db import models
# from search.models import BrStock as BrStock_S, UsStock as UsStock_S, BrRealEstate as BrRealEstate_S, UsEtf as UsEtf_S, Crypto as Crypto_S, BrTreasure as BrTreasure_S


# class BrStock(models.Model):
#     ticker = models.ForeignKey(BrStock_S, on_delete=models.PROTECT, db_index=True,
#                                related_name='vlt_br_stocks', verbose_name='Código')
#     date = models.DateField(verbose_name='Data')
#     beta = models.FloatField(blank=True, null=True, verbose_name='Beta')
#     market_cap = models.FloatField(blank=True, null=True, verbose_name='Valor de Mercado')
#     enterprise_value = models.FloatField(blank=True, null=True, verbose_name='Valor da Empresa')
#     enterprise_value_ebitda = models.FloatField(blank=True, null=True, verbose_name='VE/EBITDA')
#     trailing_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro')
#     forward_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro Projetado')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
#     class Meta:
#         ordering = ['ticker']
#         verbose_name = 'Ações BR'
#         verbose_name_plural = 'Ações BR'
    
#     def __str__(self):
#         return self.ticker


# class UsStock(models.Model):
#     ticker = models.ForeignKey(UsStock_S, on_delete=models.PROTECT, db_index=True,
#                                related_name='vlt_us_stocks', verbose_name='Código')
#     date = models.DateField(verbose_name='Data')
#     beta = models.FloatField(blank=True, null=True, verbose_name='Beta')
#     market_cap = models.FloatField(blank=True, null=True, verbose_name='Valor de Mercado')
#     enterprise_value = models.FloatField(blank=True, null=True, verbose_name='Valor da Empresa')
#     enterprise_value_ebitda = models.FloatField(blank=True, null=True, verbose_name='VE/EBITDA')
#     trailing_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro')
#     forward_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro Projetado')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
#     class Meta:
#         ordering = ['ticker']
#         verbose_name = 'Ações US'
#         verbose_name_plural = 'Ações US'
    
#     def __str__(self):
#         return self.ticker
    

# class BrRealEstate(models.Model):
#     ticker = models.ForeignKey(BrRealEstate_S, on_delete=models.PROTECT, db_index=True,
#                                related_name='vlt_br_real_estates', verbose_name='Código')
#     date = models.DateField(verbose_name='Data')
#     beta = models.FloatField(blank=True, null=True, verbose_name='Beta')
#     market_cap = models.FloatField(blank=True, null=True, verbose_name='Valor de Mercado')
#     enterprise_value = models.FloatField(blank=True, null=True, verbose_name='Valor da Empresa')
#     enterprise_value_ebitda = models.FloatField(blank=True, null=True, verbose_name='VE/EBITDA')
#     trailing_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro')
#     forward_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro Projetado')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
#     class Meta:
#         ordering = ['ticker']
#         verbose_name = 'FIIs'
#         verbose_name_plural = 'FIIs'
    
#     def __str__(self):
#         return self.ticker
    
    
# class UsEtf(models.Model):
#     ticker = models.ForeignKey(UsEtf_S, on_delete=models.PROTECT, db_index=True,
#                                related_name='vlt_us_etf', verbose_name='Código')
#     date = models.DateField(verbose_name='Data')
#     beta = models.FloatField(blank=True, null=True, verbose_name='Beta')
#     market_cap = models.FloatField(blank=True, null=True, verbose_name='Valor de Mercado')
#     enterprise_value = models.FloatField(blank=True, null=True, verbose_name='Valor da Empresa')
#     enterprise_value_ebitda = models.FloatField(blank=True, null=True, verbose_name='VE/EBITDA')
#     trailing_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro')
#     forward_p_e = models.FloatField(blank=True, null=True, verbose_name='Preço/Lucro Projetado')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
#     class Meta:
#         ordering = ['ticker']
#         verbose_name = 'ETFs US'
#         verbose_name_plural = 'ETFs US'
    
#     def __str__(self):
#         return self.ticker
    

# class Crypto(models.Model):
#     ticker = models.ForeignKey(Crypto_S, on_delete=models.PROTECT, db_index=True,
#                                related_name='vlt_cryptos', verbose_name='Código')
#     date = models.DateField(verbose_name='Data')
#     market_cap = models.FloatField(blank=True, null=True, verbose_name='Valor de Mercado')
#     circulating_suplly = models.FloatField(blank=True, null=True, verbose_name='Qtd em Circulação')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
#     class Meta:
#         ordering = ['ticker']
#         verbose_name = 'Criptomoedas'
#         verbose_name_plural = 'Criptomoedas'
    
#     def __str__(self):
#         return self.ticker
