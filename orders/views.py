from .models import Order
from rest_framework import generics
from .serializers import OrderSerializer

# Create your views here.
class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer