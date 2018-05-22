from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from decimal import Decimal


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    user_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'user_name', 'email', 'password1', 'password2', )
        #fields = ('first_name', 'middle_name', 'last_name', 'user_name', 'email','birth_date','address', 'password1', 'password2', )


class FoodsForm(forms.Form):
	fname = forms.CharField(max_length=300, required=True, label='Name')
	desc = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False, label='Description')
	other_info = forms.CharField(max_length=3000,required=False, label='Other Info')
	category = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False,label='Categories')
	price_s = forms.DecimalField(widget=forms.NumberInput(attrs={'value': 0.00}), decimal_places=2,required=False,label='Price Small')
	price_m = forms.DecimalField(widget=forms.NumberInput(attrs={'value': 0.00}), decimal_places=2,required=False,label='Price Medium')
	price_l = forms.DecimalField(widget=forms.NumberInput(attrs={'value': 0.00}), decimal_places=2,required=False,label='Price Large')
	price = forms.DecimalField(widget=forms.NumberInput(attrs={'value': 0.00}), decimal_places=2,required=False,label='Price')
	choices_status = (('1', 'Active'),('2','Inactive'))
	f_status = forms.ChoiceField(widget=forms.Select, required=False, choices=choices_status,label='status')

class FoodRatingForm(forms.Form):
	rating = forms.DecimalField(widget=forms.NumberInput(attrs={'value': 0.00}), decimal_places=2,label='Rating')
	comments = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False, label='Comments')

class UserStampsForm(forms.Form):
	order_id = forms.CharField(max_length=300, required=True , label='Order ID')
	purchase_date = forms.DateTimeField(input_formats=['%Y-%m-%d'],widget=forms.DateInput(format='%Y-%m-%d',attrs={'class':'datepicker'}), required=True, help_text='Required',label='Purchase Date')

class ContactForm(forms.Form):
	fname = forms.CharField(max_length=40, required=True, help_text='',label='Firstname')
	lname = forms.CharField(max_length=40, required=True, help_text='',label='Lastname')
	email = forms.EmailField(max_length=50, required=True, help_text='',label='Email')
	phone = forms.CharField(max_length=40, required=True, help_text='',label='Phone')
	msg = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}), required=True, help_text='',label='Message')
    