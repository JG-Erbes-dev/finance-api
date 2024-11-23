# from django.db import models


# class IncomeStatement(models.Model):
#     ticker = models.ForeignKey('search.BrStock', on_delete=models.CASCADE, db_index=True, related_name='income_statements')
#     # outros campos relacionados ao Income Statement
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.ticker

# class BalanceSheet(models.Model):
#     ticker = models.ForeignKey('search.BrStock', on_delete=models.CASCADE, db_index=True, related_name='balance_sheets')
#     # outros campos relacionados ao Balance Sheet
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.ticker

# class CashFlow(models.Model):
#     ticker = models.ForeignKey('search.BrStock', on_delete=models.CASCADE, db_index=True, related_name='cash_flows')
#     # outros campos relacionados ao Cash Flow
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.ticker