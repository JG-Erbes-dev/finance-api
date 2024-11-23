from rest_framework import serializers
from marketdata.models import BrStock, UsStock, BrRealEstate, UsEtf, Crypto, BrTreasure


exclude = ['created_at', 'updated_at']


class BrStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrStock
        exclude = exclude


class UsStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsStock
        exclude = exclude


class BrRealEstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrRealEstate
        exclude = exclude


class UsEtfSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsEtf
        exclude = exclude


class CryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crypto
        exclude = exclude


class BrTreasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrTreasure
        exclude = exclude
