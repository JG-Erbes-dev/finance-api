from django.http import JsonResponse
from . import updatesearch

def update_data_view(request):
    try:
        updatesearch()
        return JsonResponse({'status': 'success', 'message': 'Dados atualizados com sucesso!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})