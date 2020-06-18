from django.conf import settings
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
	('RP', 'Regular Pizza'),
	('SP', 'Sicilian Pizza'),
	('T', 'Topping'),
	('S', 'Sub'),
	('P', 'Pasta'),
	('D', 'Dinner Platter'),
	('Sa', 'Salad')	
)

LABEL_CHOICES = (
	('P', 'primary'),
	('S', 'secondary'),
	('D', 'danger')	
)

# Create your models here.
# class RegularPizza(models.Model):
# 	name = models.CharField(max_length=32)
# 	small = models.DecimalField(max_digits=4, decimal_places=2)
# 	large = models.DecimalField(max_digits=4, decimal_places=2)

# 	def __str__(self):
# 		return self.name


# class SicilianPizza(models.Model):
# 	name = models.CharField(max_length=32)
# 	small = models.DecimalField(max_digits=4, decimal_places=2)
# 	large = models.DecimalField(max_digits=4, decimal_places=2)


# class Topping(models.Model):
# 	name = models.CharField(max_length=32)


# class Sub(models.Model):
# 	name = models.CharField(max_length=32)
# 	small = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
# 	large = models.DecimalField(max_digits=4, decimal_places=2)


# class Pasta(models.Model):
# 	name = models.CharField(max_length=32)
# 	price = models.DecimalField(max_digits=4, decimal_places=2)

# 	def __str__(self):
# 		return self.id + ' - ' + self.name + ' is $' + self.price


# class DinnerPlatter(models.Model):
# 	name = models.CharField(max_length=32)
# 	small = models.DecimalField(max_digits=4, decimal_places=2)
# 	large = models.DecimalField(max_digits=4, decimal_places=2)

# class Salad(models.Model):
# 	name = models.CharField(max_length=32)
# 	price = models.DecimalField(max_digits=4, decimal_places=2)

class Item(models.Model):
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
	price_small = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
	has_sizes = models.BooleanField(default=False)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
	slug = models.SlugField()
	

	def __str__(self):
		return '%s | %s' % (self.category, self.title)

	def get_add_to_cart_url(self):
		return reverse("add-to-cart", kwargs={
			'slug': self.slug
		})

	def get_remove_from_cart_url(self):
		return reverse("remove-from-cart", kwargs={
			'slug': self.slug
		})	


class OrderItem(models.Model):
	SIZE_CHOICES = [
		('Large', 'Large'),
		('Large', 'Small')
	]
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	size = models.CharField(max_length=5, choices=SIZE_CHOICES, blank=True, null=True)
	quantity = models.IntegerField(default=1)
	
	def __str__(self):
		if self.item.has_sizes == True:
			return '%s x %s %s %s' % (self.quantity, self.size, self.item.title, self.item.category)
		else:
			return '%s x %s' % (self.quantity, self.item.title)

	def get_total_item_price(self):
		return self.quantity * self.item.price

	def get_total_small_item_price(self):
		return self.quantity * self.item.price_small

	def get_final_price(self):
		if self.item.price_small:
			return self.get_total_small_item_price()
		return self.get_total_item_price()

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add = True)
	ordered_date = models.DateTimeField
	ordered = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user.username

	def cart_item_count(self, user):
		if user.is_authenticated:
			qs = self.objects.filter(user=user, ordered=False)
			if qs.exists():
				return qs[0].items.count()
		return 0

	def get_total(self):
		total = 0
		for order_item in self.items.all():
			total += order_item.get_final_price()
		return total