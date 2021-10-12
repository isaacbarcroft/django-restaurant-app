from rest_framework import serializers 
from .models import Menuitem

class MenuitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menuitem
         # fields = '__all__'
        fields = ('id','title', 'category', 'price', 'desc')

            
        def dollar_amount(self):
            return "$%s" % self.price if self.price else "" 