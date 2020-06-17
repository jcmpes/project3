from django.urls import path

from . import views

from .views import add_to_cart, remove_from_cart


urlpatterns = [
    path("", views.index, name="index"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart')

]
