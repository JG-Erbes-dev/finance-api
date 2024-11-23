from django.urls import path
from . import views


urlpatterns = [
    path('stock/br/', views.BrStockListCreateView.as_view(), name='br-stock-list'),
    path('stock/br/<str:ticker>/', views.BrStockRetrieveUpdateDestroyView.as_view(), name='br-stock-detail'),

    path('stock/us/', views.UsStockListCreateView.as_view(), name='us-stock-list'),
    path('stock/us/<str:ticker>/', views.UsStockRetrieveUpdateDestroyView.as_view(), name='us-stock-detail'),

    path('real-estate/br/', views.BrRealEstateListCreateView.as_view(), name='br-real-estate-list'),
    path('real-estate/br/<str:ticker>/', views.BrRealEstateRetrieveUpdateDestroyView.as_view(), name='br-real-estate-detail'),

    path('etf/us/', views.UsEtfListCreateView.as_view(), name='us-etf-list'),
    path('etf/us/<str:ticker>/', views.UsEtfRetrieveUpdateDestroyView.as_view(), name='us-etf-detail'),

    path('crypto/', views.CryptoListCreateView.as_view(), name='cryptos-list'),
    path('crypto/<str:ticker>/', views.CryptoRetrieveUpdateDestroyView.as_view(), name='cryptos-detail'),

    path('treasure/br/', views.BrTreasureListCreateView.as_view(), name='tresure-br-list'),
    path('treasure/br/<str:ticker>/', views.BrTreasureRetrieveUpdateDestroyView.as_view(), name='tresure-br-detail'),

    path('stats/', views.MarketDataStatsView.as_view(), name='marketdata-stats-view'),
    path('stats/stock/br/', views.MarketDataStatsView.as_view(), name='br-stock-stats-view'),
    path('stats/stock/us/', views.MarketDataStatsView.as_view(), name='us-stock-stats-view'),
    path('stats/realestate/br/', views.MarketDataStatsView.as_view(), name='br-real-estate-stats-view'),
    path('stats/etf/us/', views.MarketDataStatsView.as_view(), name='us-etf-stats-view'),
    path('stats/crypto/', views.MarketDataStatsView.as_view(), name='cryptos-stats-view'),
    path('stats/treasure/br/', views.MarketDataStatsView.as_view(), name='tresure-br-stats-view'),
]
