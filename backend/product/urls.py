from django.urls import path

from . import views

urlpatterns = [
    path('product/create/', views.CreateProduct.as_view()),
    path('product/remove/', views.RemoveProduct.as_view()),
    path('product/edit/', views.EditProduct.as_view()),
    path('product_list/create/', views.CreateProductList.as_view()),
    path('product_list/remove/', views.RemoveProductList.as_view()),
    path('product_list/add_product/', views.AddProductToList.as_view()),
    path('product_list/add_products/', views.AddMultiplesProductsToList.as_view()),
    path('product_list/remove_product/', views.RemoveOneProductFromList.as_view()),
    path('product_list/remove_products/', views.RemoveMultiplesProductsFromList.as_view()),
]