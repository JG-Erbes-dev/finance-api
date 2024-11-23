from rest_framework import serializers
from econdata.models import BrInterestRate, UsInterestRate, BrCDI, CumulativeBrCDI, BrInflation, CumulativeBrInflation, UsInflation, DollarExchangeRate, CommodityPrice


fields = ['date', 'value']


class BrInterestRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrInterestRate
        fields = fields


class UsInterestRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsInterestRate
        fields = fields


class BrCDISerializer(serializers.ModelSerializer):

    class Meta:
        model = BrCDI
        fields = fields


class CumulativeBrCDISerializer(serializers.ModelSerializer):

    class Meta:
        model = CumulativeBrCDI
        fields = fields


class BrInflationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrInflation
        fields = fields


class CumulativeBrInflationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CumulativeBrInflation
        fields = fields


class UsInflationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsInflation
        fields = fields


class DollarExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DollarExchangeRate
        fields = fields


class CommodityPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommodityPrice
        fields = fields
