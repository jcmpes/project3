from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.utils import timezone
from .models import Item, OrderItem, Order, Topping

# Create your views here.
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'orders/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order.")
            return redirect("/")

def index(request):
	if not request.user.is_authenticated:
		return render(request, "registration/login.html", {"message": None})
	context = {
		'user': request.user,
		'regular_pizzas': Item.objects.filter(category='RP'),
        'sicilian_pizzas': Item.objects.filter(category='SP'),
        'toppings': Item.objects.filter(category='T'),
        'subs': Item.objects.filter(category='S'),
        'pastas': Item.objects.filter(category='P'),
        'dinner_platters': Item.objects.filter(category='D'),
        'salads': Item.objects.filter(category='Sa'),
	}
	return render(request, "orders/index.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "registration/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "registration/login.html", {"message": "Logged out."})

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", context)

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, size="Large", user=request.user, ordered=False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order.
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was added to your cart.")
            order.items.add(order_item)
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("order-summary")

@login_required
def add_small_to_cart(request, slug_small):
    item = get_object_or_404(Item, slug_small=slug_small)
    order_item, created = OrderItem.objects.get_or_create(item=item, size="Small", user=request.user, ordered=False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order.
        if order.items.filter(item__slug_small=item.slug_small).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was added to your cart.")
            
            order.items.add(order_item)
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order.
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, size="Large", user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("/", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("/", slug=slug)

@login_required
def remove_small_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order.
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, size="Small", user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("/", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("/", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order.
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, size="Large", user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "The item's quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("/", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("/", slug=slug)
    return redirect("/", slug=slug)

@login_required
def remove_single_small_item_from_cart(request, slug_small):
    item = get_object_or_404(Item, slug_small=slug_small)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order.
        if order.items.filter(item__slug_small=item.slug_small).exists():
            order_item = OrderItem.objects.filter(item=item, size="Small", user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "The item's quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("/", slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect("/", slug=slug)
    return redirect("/", slug=slug)


@login_required
def order_item(request, order_item_id):
    try:
        order_item = OrderItem.objects.get(pk=order_item_id)
    except ObjectDoesNotExist:
        messages.error(self.request, "Order Item does not exist.")
        return redirect("/")
    context = {
        "order_item": order_item,
        'toppings': Topping.objects.all() 
    }
    return render(request, "orders/order_item.html", context)


@login_required
def add_topping(request, order_item_id):
    try:
        topping_id = int(request.POST['topping'])
        topping = Topping.objects.get(pk=topping_id)
        order_item = OrderItem.objects.get(pk=order_item_id)
    except KeyError:
        messages.info(request, "KeyError.")
        return redirect("orders/order_item.html")
    
    topping.orderitems.add(order_item)
    return HttpResponseRedirect(reverse("order_item", args=(order_item_id,)))


@login_required
def remove_toppings(request, order_item_id):
    try:
        order_item = OrderItem.objects.get(pk=order_item_id)
        qs = order_item.toppings.all().values_list('pk', flat=True)

    except KeyError:
        messages.info(request, "KeyError.")
        return redirect("orders/order_item.html")

    for i in range(qs.count()):
        order_item.toppings.remove(qs[0])
    return HttpResponseRedirect(reverse("order_item", args=(order_item_id,)))