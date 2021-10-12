from django.urls import path, include

app_name = 'api_v1'
#corresponding to namespace in settings.urls

urlpatterns = [
    path('menuitems/', include('menuitems.urls',  namespace='menuitems')),
    path('orders/', include('orders.urls',  namespace='orders')),
]