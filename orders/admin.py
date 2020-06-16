from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Topping, Sub, Pasta, DinnerPlatter, Salad, Item, OrderItem, Order

# Register your models here.
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(DinnerPlatter)
admin.site.register(Salad)

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)