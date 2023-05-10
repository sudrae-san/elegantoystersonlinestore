from django.shortcuts import render

from oyster.models import *
from account.models import Account
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def home_screen_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request,"oyster/home.html",context)

def home_screen_view(request):
 	context={}
 	products=Product.objects.all()
 	context['products'] = products
 	return render(request,"oyster/home.html",context)




def cart_view(request):

	if request.user.is_authenticated:
		username = request.user.username 
		order, created = Order.objects.get_or_create(username=username,complete=False)

	else:
		items=[]

	context={'items':items}

	return render(request,"oyster/cart.html",context)

def checkout_view(request):
	context={}
	return render(request,"oyster/checkout.html",context)

