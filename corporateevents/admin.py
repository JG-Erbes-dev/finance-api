from django.contrib import admin
from .models import BrStock, UsStock, BrRealEstate, UsEtf


for model in [BrStock, UsStock, BrRealEstate, UsEtf]:

    filter_field = 'ticker'

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
