from rest_framework import generics 
from .models import Menuitem
from .serializers import MenuitemSerializer

# Create your views here.

# takes a request and returns a response
# request handler
class MenuitemsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuitemSerializer

class MenuitemsDetailsAPIView(generics.ListAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuitemSerializer