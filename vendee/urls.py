from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeliveryOrderItemListView.as_view(), name='order_item_list_view'),
    path('create-order/item/', views.CreateDeliveryOrderItem.as_view(), name='create_order_item'),
]
