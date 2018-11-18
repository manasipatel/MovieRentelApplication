from django.db import models

# Create your models here.

class Customertable(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email_id = models.EmailField(max_length=20)
	phone_no = models.CharField(max_length=12)
	address1 = models.CharField("Address line 1",max_length=100,)
	address2 = models.CharField("Address line 2",max_length=100, null=True, blank = True)
	city =models.CharField(max_length=21)
	zip_code = models.CharField(max_length=6)
	country = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name


class Movietable(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	released_date = models.DateTimeField(auto_now_add=False)
	category = models.CharField(max_length=15)
	customer = models.ForeignKey(Customertable, on_delete=models.SET_NULL, null=True, blank = True)


	def __str__(self):
		return self.name


