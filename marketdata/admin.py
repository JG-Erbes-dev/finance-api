from django.contrib import admin
from .models import BrStock, UsStock, BrRealEstate, UsEtf, Crypto, BrTreasure


for model in [BrStock, UsStock, BrRealEstate, UsEtf, Crypto, BrTreasure]:

    if model != BrTreasure:
        filter_field = 'ticker'
    else:
        filter_field = 'title'

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
                ],
                "list_filter": (filter_field,)
            },
        ),
    )
