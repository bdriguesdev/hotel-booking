from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from .models import Product, ProductList
from .serializers import ProductSerializer, ProductListSerializer
from backend.validators import textValidator, numValidator
from backend.hotel.models import Hotel

class CreateProduct(APIView):

    #Need to check if the user is a business acount
    #image of the product?
    def post(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            name = textValidator(request.data['name'], 30, 4)
            price = numValidator(request.data['price'], 1000, 0.1)
            description = textValidator(request.data['description'], 50)
            product = Product(name=name, price=price, description=description, created=timezone.now(), updated=timezone.now(), business=request.authorized)
            product.save()
            serializer = ProductSerializer(product)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid product.')

class RemoveProduct(APIView):

    #check if the business has this product
    def delete(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_id = request.data['productId'] #validate
            product = Product.objects.get(id=product_id)
            if request.authorized != product.business:
                raise Exception

            product.delete()
            serializer = ProductSerializer(product)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid product.')
        
class EditProduct(APIView):

    def update(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_id = request.data['productId'] #validate
            product = Product.objects.get(id=product_id)
            if request.authorized != product.business:
                raise Exception

            if request.data['name'] != " ":
                product.name = textValidator(request.data['name'], 30, 4)
            if request.data['price'] != " ":
                product.price = numValidator(request.data['price'], 1000, 0.1)
            if request.data['description'] != " ":
                product.description = textValidator(request.data['description'], 50)
            product.updated = timezone.now()
            product.save()
            serializer = ProductSerializer(product)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid text.')


class CreateProductList(APIView):

    def post(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception       

            name = textValidator(request.data['name'], 30, 4)
            product_list = ProductList(name=name, created=timezone.now(), updated=timezone.now(), business=request.authorized)
            product_list.save()
            serializer = ProductListSerializer(productlist)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid product list.')

class RemoveProductList(APIView):

    #check if the business/hotel has this product list and don't delete all the products from db
    def delete(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_list_id = request.data['productListId']
            product_list = ProductList.objects.get(id=product_list_id)
            if product_list.business != request.authorized:
                raise Exception

            product_list.delete()
            serializer = ProductListSerializer(product_list)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class AddProductToList(APIView):

    #check if the business/hotel has this product list and the product
    def post(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_list_id = request.data['productListId']
            product_id = request.data['productId']

            product_list = ProductList.objects.get(id=product_list_id)
            if product_list.business != request.authorized:
                raise Exception

            product = Product.objects.get(id=product_id)
            if product.business != request.authorized:
                raise Exception

            product_list.products.add(product)
            product_list.updated = timezone.now()
            product_list.save()
            serializer = ProductListSerializer(product_list)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class AddMultiplesProductsToList(APIView):

    def post(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_list_id = request.data['productListId']

            product_list = ProductList.objects.get(id=product_list_id)
            if product_list.business != request.authorized:
                raise Exception

            if len(request.data['products']) <= 0:
                raise Exception

            for x in range(0, len(request.data['products'])):
                if not isinstance(request.data['products'][x], int):
                    raise Exception
                
                product_id = request.data['products'][x]
                product = Product.objects.get(id=product_id)
                if product_list in product.product_lists:
                    raise Exception
                
                product_list.products.add(product)

            product_list.updated = timezone.now()
            product_list.save()
            serializer = ProductListSerializer(product_list)

            return Response(serializer.data)
        except Exception:
            return Response('An error has been occurred.')

class RemoveOneProductFromList(APIView):

    #check if the business/hotel has this product list and the list has the product
    def delete(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_list_id = request.data['productListId']
            product_id = request.data['productId']

            product_list = ProductList.objects.get(id=product_list_id)
            if product_list.business != request.authorized:
                raise Exception

            product = Product.objects.get(id=product_id)
            if product.business != request.authorized:
                raise Exception

            product_list.products.remove(product)
            product_list.updated = timezone.now()
            product_list.save()
            serializer = ProductListSerializer(product_list)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class RemoveMultiplesProductsFromList(APIView):

    #check if the business/hotel has this product list and the list has the product
    def delete(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            product_list_id = request.data['productListId']

            product_list = ProductList.objects.get(id=product_list_id)
            if product_list.business != request.authorized:
                raise Exception

            if len(request.data['products']) <= 0:
                raise Exception

            for x in range(0, len(request.data['products'])):
                if not isinstance(request.data['products'][x], int):
                    raise Exception
                
                product_id = request.data['products'][x]

                product = Product.objects.get(id=product_id)
                if not (product_list in product.product_lists):
                    raise Exception
                product_list.products.remove(product)

            product_list.updated = timezone.now()
            product_list.save()
            serializer = ProductListSerializer(product_list)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')
