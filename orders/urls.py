from django.urls import path

from . import views

from .views import add_to_cart, add_small_to_cart, remove_from_cart, OrderSummaryView, remove_single_item_from_cart


urlpatterns = [
    path("", views.index, name="index"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-small-to-cart/<slug_small>/', add_small_to_cart, name='add-small-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary')

]
