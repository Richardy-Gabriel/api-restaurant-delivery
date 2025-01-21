from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restaurant import models, serializers


@api_view(['GET', 'POST'])
def product_list_create(request):
    """
    List and Create Products
    """
    if request.method == 'POST':
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    products = models.ProductModel.objects.all()
    serializer = serializers.ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = models.ProductModel.objects.get(pk=pk)
    except models.ProductModel.DoesNotExist:
        return Response({
            "error": "The product is not registered"
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.active = False
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = serializers.ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET','POST'])
def client_list_create(request):
    """
    List and Create Clients
    """
    if request.method == 'POST':
        serializer = serializers.ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    clients = models.ClientModel.objects.all()
    serializer = serializers.ClientSerializer(clients, many=True)
    return Response(serializer.data)
