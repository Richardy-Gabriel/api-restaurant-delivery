from django.urls import path
from restaurant import views

urlpatterns = [
    path('products/', views.product_list_create, name="product-list-create"),
]
