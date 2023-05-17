from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Aboutus (View):
    def get(self, request):
        return render (request, 'aboutus.html')
