from django.urls import path
from restaurant import views

urlpatterns = [
    path('products/', views.product_list_create, name="product-list-create"),
    path('products/<int:pk>/', views.product_detail, name="product-detail"),
    
    path('clients/', views.client_list_create, name="client-list-create"),
]
