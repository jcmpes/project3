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


class DinnerPlatter(models.Model):
	name = models.CharField(max_length=32)
	small = models.DecimalField(max_digits=4, decimal_places=2)
	large = models.DecimalField(max_digits=4, decimal_places=2)

class Salad(models.Model):
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=4, decimal_places=2)
