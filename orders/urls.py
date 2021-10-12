from django.urls import path
from .views import OrdersAPIView

app_name = 'orders'

urlpatterns = [ 
    path('', OrdersAPIView.as_view(), name='order_list')
]