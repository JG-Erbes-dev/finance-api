from django.urls import path
from . import views

urlpatterns = [
    path('interest-rate/br/', views.BrInterestRateListCreateView.as_view(), name='br-interest-rate-list'),
    path('interest-rate/br/<int:pk>/', views.BrInterestRateRetrieveUpdateDestroyView.as_view(), name='br-interest-rate-detail'),

    path('interest-rate/us/', views.UsInterestRateListCreateView.as_view(), name='us-interest-rate-list'),
    path('interest-rate/us/<int:pk>/', views.UsInterestRateRetrieveUpdateDestroyView.as_view(), name='us-interest-rate-detail'),

    path('cdi/br/', views.BrCDIListCreateView.as_view(), name='br-cdi-list'),
    path('cdi/br/<int:pk>/', views.BrCDIRetrieveUpdateDestroyView.as_view(), name='br-cdi-detail'),

    path('cdi/br/cumulative/', views.CumulativeBrCDIListCreateView.as_view(), name='br-cumulative-cdi-list'),
    path('cdi/br/cumulative/<int:pk>/', views.CumulativeBrCDIRetrieveUpdateDestroyView.as_view(), name='br-cumulative-cdi-detail'),

    path('inflation/br/', views.BrInflationListCreateView.as_view(), name='br-inflation-list'),
    path('inflation/br/<int:pk>/', views.BrInflationRetrieveUpdateDestroyView.as_view(), name='br-inflation-detail'),

    path('inflation/br/cumulative/', views.CumulativeBrInflationListCreateView.as_view(), name='br-cumulative-inflation-list'),
    path('inflation/br/cumulative/<int:pk>/', views.CumulativeBrInflationRetrieveUpdateDestroyView.as_view(), name='br-cumulative-inflation-detail'),

    path('inflation/us/', views.UsInflationListCreateView.as_view(), name='us-inflation-list'),
    path('inflation/us/<int:pk>/', views.UsInflationRetrieveUpdateDestroyView.as_view(), name='us-inflation-detail'),

    path('exchange/dollar-rate/', views.DollarExchangeRateListCreateView.as_view(), name='dollar-rate-list'),
    path('exchange/dollar-rate/<int:pk>/', views.DollarExchangeRateRetrieveUpdateDestroyView.as_view(), name='dollar-rate-detail'),

    path('commodities/price/', views.CommodityPriceListCreateView.as_view(), name='crypto-data-list'),
    path('commodities/price/<int:pk>/', views.CommodityPriceRetrieveUpdateDestroyView.as_view(), name='crypto-data-detail'),
]
