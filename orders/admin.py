from django.contrib import admin

from .models import Item, OrderItem, Order, Topping

# Register your models here.
class ToppingInline(admin.StackedInline):
    model = Topping.orderitems.through
    extra = 1

class OrderItemAdmin(admin.ModelAdmin):
    inlines = [ToppingInline]

admin.site.register(Item)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order)
admin.site.register(Topping)