from rest_framework import serializers
from restaurant import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'
