import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import csrf
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
# Product Views

def testProduct(request):
    return JsonResponse({"STATUS": "Working"})


# post
@csrf_exempt
def createNewProduct(request):
    json_data = json.loads(request.body)
    newProduct = ProductMainModel()
    newProduct.title = json_data["title"]
    newProduct.description = json_data["description"]
    newProduct.price = json_data["price"]
    newProduct.save()
    return JsonResponse({"data": newProduct.unique_id})


# get
def getAllProductsWImages(request):
    product_list = ProductMainModel.objects.all().values()
    p_list = []
    for product in product_list:
        p_list.append({"unique_id": product["unique_id"], "title": product["title"]})
    return JsonResponse({"data": p_list})


def createNewProductsWithImages():
    pass


@csrf_exempt
def addProductToCart(request, unique_id, user_id):
    newCartModel = CartModel()
    product = ProductMainModel.objects.filter(unique_id=unique_id).values()
    for d in product:
        print(d)
        newCartModel.owner = user_id
        newCartModel.price = d["price"]
        newCartModel.products = unique_id
        newCartModel.save()
        break
    return JsonResponse({"status": newCartModel.id})


@csrf_exempt
def testUploadImage(request):
    print(request)
    pass
