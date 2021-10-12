from django.urls import path
from .views import OrdersAPIView

urlpatterns = [ 
    path('', OrdersAPIView.as_view(), name='order_list')
]