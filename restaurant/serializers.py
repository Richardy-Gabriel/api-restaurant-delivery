from rest_framework import serializers
from restaurant import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True
            },
            'cpf': {
                'write_only': True
            },
        }
        model = models.ClientModel
        fields = '__all__'
