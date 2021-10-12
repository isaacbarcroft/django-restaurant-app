from django.urls import path
from .views import MenuitemsAPIView
from . import views

app_name = 'menuitems'

urlpatterns = [
    path('<int:pk>/', views.MenuitemsAPIView.as_view(), name ="menuitem_list"),
    path('', views.MenuitemsDetailsAPIView.as_view(), name='menuitem_detail')
]