from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from econdata.models import BrInterestRate, UsInterestRate, BrCDI, CumulativeBrCDI, BrInflation, CumulativeBrInflation, UsInflation, DollarExchangeRate, CommodityPrice
from econdata.serializers import BrInterestRateSerializer, UsInterestRateSerializer, BrCDISerializer, CumulativeBrCDISerializer, BrInflationSerializer, CumulativeBrInflationSerializer, UsInflationSerializer, DollarExchangeRateSerializer, CommodityPriceSerializer


class BrInterestRateListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrInterestRate.objects.all()
    serializer_class = BrInterestRateSerializer


class BrInterestRateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrInterestRate.objects.all()
    serializer_class = BrInterestRateSerializer


class UsInterestRateListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsInterestRate.objects.all()
    serializer_class = UsInterestRateSerializer


class UsInterestRateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsInterestRate.objects.all()
    serializer_class = UsInterestRateSerializer


class BrCDIListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrCDI.objects.all()
    serializer_class = BrCDISerializer


class BrCDIRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrCDI.objects.all()
    serializer_class = BrCDISerializer


class CumulativeBrCDIListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CumulativeBrCDI.objects.all()
    serializer_class = CumulativeBrCDISerializer


class CumulativeBrCDIRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CumulativeBrCDI.objects.all()
    serializer_class = CumulativeBrCDISerializer


class BrInflationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrInflation.objects.all()
    serializer_class = BrInflationSerializer


class BrInflationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrInflation.objects.all()
    serializer_class = BrInflationSerializer


class CumulativeBrInflationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CumulativeBrInflation.objects.all()
    serializer_class = CumulativeBrInflationSerializer


class CumulativeBrInflationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CumulativeBrInflation.objects.all()
    serializer_class = CumulativeBrInflationSerializer


class UsInflationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsInflation.objects.all()
    serializer_class = UsInflationSerializer


class UsInflationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsInflation.objects.all()
    serializer_class = UsInflationSerializer


class DollarExchangeRateListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DollarExchangeRate.objects.all()
    serializer_class = DollarExchangeRateSerializer


class DollarExchangeRateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DollarExchangeRate.objects.all()
    serializer_class = DollarExchangeRateSerializer


class CommodityPriceListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CommodityPrice.objects.all()
    serializer_class = CommodityPriceSerializer


class CommodityPriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CommodityPrice.objects.all()
    serializer_class = CommodityPriceSerializer
