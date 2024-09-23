from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #My apps
    path('api/v1/products/', include('apps.products.urls'))
]
