from django.db import models
from django.contrib.auth.models import User

from decimal import Decimal
from django.utils import timezone

# Create your models here.




class Foods(models.Model):
	fname = models.CharField(max_length=300, verbose_name='Name')
	desc = models.TextField(verbose_name='Description')
	other_info = models.CharField(max_length=3000, verbose_name='Other Info')
	category = models.TextField(verbose_name='Categories')
	price_s = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='Price Small')
	price_m = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='Price Medium')
	price_l = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='Price Large')
	price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='Price')
	choices_status = (('1', 'Active'),('2','Inactive'))
	f_status = models.CharField(max_length=200, default='1', choices=choices_status,verbose_name='status')
	date_created = models.DateTimeField(("Date Created"), default=timezone.now)


class FoodRating(models.Model):
	fid = models.ForeignKey(Foods, on_delete=models.CASCADE,verbose_name='Food ID', default=None)
	usr = models.ForeignKey(User,verbose_name='User ID', default=None)
	rating = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='rating')
	choices_status = (('1', 'Approved'),('2','Declined'),('3','Pending'))
	r_status = models.CharField(max_length=200, default='3', choices=choices_status,verbose_name='status')
	comments = models.TextField(verbose_name='Comments')


class UserStamps(models.Model):
	usr = models.ForeignKey(User,verbose_name='User ID', default=None)
	choices_status = (('1', 'Approved'),('2','Declined'),('3','Pending'),('4','Claimed'))
	status = models.CharField(max_length=200, default='3', choices=choices_status,verbose_name='status')
	order_id = models.CharField(max_length=300, default='000000', verbose_name='Order ID')
	purchase_date = models.DateTimeField(("Purchase Date"), default=timezone.now)
	date_created = models.DateTimeField(("Date Created"), default=timezone.now)


# class BookCatering(models.Model):
# 	usr = models.ForeignKey(User,verbose_name='User ID', default=None)
# 	foods = models.OneToMany(Foods)
# 	date_event = models.DateTimeField(("Event Date"), default=timezone.now)
# 	date_created = models.DateTimeField(("Date Created"), default=timezone.now)

# class BookTable(models.Model):
# 	usr = models.ForeignKey(User,verbose_name='User ID', default=None)
# 	#pax = models.IntegerField
# 	date_book = models.DateTimeField(("Book Date"), default=timezone.now)
# 	date_created = models.DateTimeField(("Date Created"), default=timezone.now)

class Contact(models.Model):
	fname = models.CharField(max_length=40, verbose_name='Firstname')
	lname = models.CharField(max_length=40, verbose_name='Lastname')
	email = models.EmailField(max_length=50, verbose_name='Email Address')
	phone = models.CharField(max_length=100, verbose_name='Firstname')
	msg = models.TextField(verbose_name='Message')