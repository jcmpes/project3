from django.urls import path

from . import views

from .views import (
    index,
    add_to_cart,
    add_small_to_cart,
    remove_from_cart,
    remove_small_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    remove_single_small_item_from_cart,
    order_item,
    add_topping,
    remove_toppings,
    checkout,
    orders
)


urlpatterns = [
    path('', index, name="index"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-small-to-cart/<slug_small>/', add_small_to_cart, name='add-small-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-small-from-cart/<slug>/', remove_small_from_cart, name='remove-small-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('remove-small-item-from-cart/<slug_small>/', remove_single_small_item_from_cart, name='remove-single-small-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('<int:order_item_id>', order_item, name='order_item'),
    path('<int:order_item_id>/add_topping', add_topping, name='add_topping'),
    path('<int:order_item_id>/remove_toppings', remove_toppings, name='remove_toppings'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders')

]
