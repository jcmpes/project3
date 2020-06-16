from django.conf import settings
from django.db import models

# Create your models here.
class RegularPizza(models.Model):
	name = models.CharField(max_length=32)
	small = models.DecimalField(max_digits=4, decimal_places=2)
	large = models.DecimalField(max_digits=4, decimal_places=2)


class SicilianPizza(models.Model):
	name = models.CharField(max_length=32)
	small = models.DecimalField(max_digits=4, decimal_places=2)
	large = models.DecimalField(max_digits=4, decimal_places=2)


class Topping(models.Model):
	name = models.CharField(max_length=32)


class Sub(models.Model):
	name = models.CharField(max_length=32)
	small = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
	large = models.DecimalField(max_digits=4, decimal_places=2)


class Pasta(models.Model):
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return self.id + ' - ' + self.name + ' is $' + self.price


class DinnerPlatter(models.Model):
	name = models.CharField(max_length=32)
	small = models.DecimalField(max_digits=4, decimal_places=2)
	large = models.DecimalField(max_digits=4, decimal_places=2)

class Salad(models.Model):
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=4, decimal_places=2)

class Item(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField()

	def __str__(self):
		return self.title

class OrderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add = True)
	ordered_date = models.DateTimeField
	ordered = models.BooleanField(default=False)
	def __str__(self):
		return self.user.username