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





def checkout_view(request):
	context={}
	return render(request,"oyster/checkout.html",context)

