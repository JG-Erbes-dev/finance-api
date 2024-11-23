from django.contrib import admin
from econdata.models import BrInterestRate, UsInterestRate, BrInflation, CumulativeBrInflation, UsInflation, DollarExchangeRate, CommodityPrice


for model in [BrInterestRate, UsInterestRate, BrInflation, CumulativeBrInflation,
              UsInflation, DollarExchangeRate, CommodityPrice]:
    admin.site.register(
        model,
        type(
            f"{model.__name__}Admin",
            (admin.ModelAdmin,),
            {
                "list_display": [
                    field.name
                    for field in model._meta.fields
                    if field.name not in ("created_at", "updated_at")
                ]
            },
        ),
    )
