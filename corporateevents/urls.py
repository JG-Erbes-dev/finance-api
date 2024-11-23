from django.urls import path
from . import views


urlpatterns = [
    path('events/stock/br/', views.BrStockListCreateView.as_view(), name='events-br-stock-list'),
    path('events/stock/br/<str:ticker>/', views.BrStockRetrieveUpdateDestroyView.as_view(), name='events-br-stock-detail'),

    path('events/stock/us/', views.UsStockListCreateView.as_view(), name='events-us-stock-list'),
    path('events/stock/us/<str:ticker>/', views.UsStockRetrieveUpdateDestroyView.as_view(), name='events-us-stock-detail'),

    path('events/realestate/br/', views.BrRealEstateListCreateView.as_view(), name='events-br-real-estate-list'),
    path('events/realestate/br/<str:ticker>/', views.BrRealEstateRetrieveUpdateDestroyView.as_view(), name='events-br-real-estate-detail'),

    path('events/etf/us/', views.UsEtfListCreateView.as_view(), name='events-us-etf-list'),
    path('events/etf/us/<str:ticker>/', views.UsEtfRetrieveUpdateDestroyView.as_view(), name='events-us-etf-detail'),
]
