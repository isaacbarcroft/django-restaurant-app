from django.urls import path
from .views import OrderAPIView

urlpatterns = [ 
    path('', OrderAPIView.as_views(), name='order_list')
]