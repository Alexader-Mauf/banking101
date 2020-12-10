from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Transfer, Customer, Account
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. This is the index.")




def testview(request):
    output = Customer.objects.all()
    return HttpResponse(output)