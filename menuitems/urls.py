from django.urls import path
from .views import MenuitemsAPIView



urlpatterns = [
    path('', MenuitemsAPIView.as_view(), name ="menuitem_list")
]