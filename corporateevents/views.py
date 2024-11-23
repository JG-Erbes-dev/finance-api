from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from corporateevents.models import BrStock, UsStock, BrRealEstate, UsEtf
from corporateevents.serializers import BrStockSerializer, UsStockSerializer, BrRealEstateSerializer, UsEtfSerializer


class BrStockListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrStock.objects.all()
    serializer_class = BrStockSerializer


class BrStockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrStock.objects.all()
    serializer_class = BrStockSerializer


class UsStockListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsStock.objects.all()
    serializer_class = UsStockSerializer


class UsStockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsStock.objects.all()
    serializer_class = UsStockSerializer


class BrRealEstateListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrRealEstate.objects.all()
    serializer_class = BrRealEstateSerializer


class BrRealEstateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrRealEstate.objects.all()
    serializer_class = BrRealEstateSerializer


class UsEtfListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsEtf.objects.all()
    serializer_class = UsEtfSerializer


class UsEtfRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UsEtf.objects.all()
    serializer_class = UsEtfSerializer
