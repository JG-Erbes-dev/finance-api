from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from marketdata.models import BrStock, UsStock, BrRealEstate, UsEtf, Crypto, BrTreasure, Stats
from marketdata.serializers import BrStockSerializer, UsStockSerializer, BrRealEstateSerializer, UsEtfSerializer, CryptoSerializer, BrTreasureSerializer


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


class CryptoListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer


class CryptoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer


class BrTreasureListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrTreasure.objects.all()
    serializer_class = BrTreasureSerializer


class BrTreasureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BrTreasure.objects.all()
    serializer_class = BrTreasureSerializer


class MarketDataStatsView(views.APIView):

    def get(self, request, *args, **kwargs):
        resultados = {}
        soma_total_ativos = 0

        path_segments = request.path.split('/')
        if len(path_segments) > 5:
            model_mapping = {
                'stock/br': 'brstock',
                'stock/us': 'usstock',
                'realestate/br': 'brrealestate',
                'etf/us': 'usetf',
                'crypto': 'crypto',
                'treasure/br': 'brtreasure'
            }

            model_key = '/'.join(path_segments[4:])
            model_key = model_key.rstrip('/')
            print(f'Obtido model_key: {model_key}')

            if model_key not in model_mapping:
                print(f'Modelo "{model_key}" não encontrado no mapeamento.')
                return response.Response({'detail': 'Model não encontrado'}, status=status.HTTP_404_NOT_FOUND)

            model_name = model_mapping[model_key]
            stats = Stats.objects.filter(model=model_name)

            if not stats.exists():
                print(f'Modelo "{model_name}" não encontrado na tabela Stats.')
                return response.Response({'detail': 'Model não encontrado'}, status=status.HTTP_404_NOT_FOUND)

            total_ativos = stats.values('ticker').distinct().count()

            ativos = []
            if total_ativos > 0:
                ativos = stats.values('ticker', 'data_inicio')

            resultados[model_name] = {
                'total_ativos': total_ativos,
                'ativos': ativos
            }

            return response.Response(data=resultados, status=status.HTTP_200_OK)

        elif len(path_segments) == 5:
            modelos = ['brstock', 'usstock', 'brrealestate', 'usetf', 'crypto', 'brtreasure']

            for model_name in modelos:
                stats = Stats.objects.filter(model=model_name)

                total_ativos = stats.values('ticker').distinct().count()

                resultados[model_name] = {
                    'total_ativos': total_ativos,
                }

                soma_total_ativos += total_ativos

            resultados['ativos_em_base'] = soma_total_ativos

            return response.Response(data=resultados, status=status.HTTP_200_OK)

        else:
            return response.Response({'detail': 'URL inválida'}, status=status.HTTP_400_BAD_REQUEST)
