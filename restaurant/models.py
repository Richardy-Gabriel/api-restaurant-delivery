from django.db import models


class BaseModel(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ProductModel(BaseModel):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)


class ClientModel(BaseModel):
    name = models.CharField(max_length=180, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    street = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=155, null=False)
    number = models.PositiveIntegerField(null=False)
    state = models.CharField(max_length=2, null=False)
    city = models.CharField(max_length=100, null=False)
    contact = models.IntegerField(null=False)
    email = models.EmailField(unique=True)
