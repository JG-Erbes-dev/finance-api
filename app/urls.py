from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('corporateevents.urls')),
    path('api/v1/', include('econdata.urls')),
    path('api/v1/', include('marketdata.urls')),
    path('api/v1/', include('search.urls')),
    path('api/v1/', include('updatedata.urls')),
]
