from rest_framework import viewsets, status
from rest_framework.views import APIView

# Create your views here.
from rest_framework.response import Response

from .models import Product, User
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ViewSet):

    # /api/products
    def list(self, request):
        product = Product.objects.all()
        # print("Value is coming here")
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    # /api/products
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:id>
    def retrieve(self, request, pk = None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # /api/products/<str:id>
    def update(self, request, pk = None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:id>
    def destroy(self, request, pk = None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self,_):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id' : user.id
        })

