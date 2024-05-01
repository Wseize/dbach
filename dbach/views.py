from django.shortcuts import render
from rest_framework import  viewsets,status
from .models import Category, MessageList, Order, OrderedProduct, Product, Logo,Message, ProductImage, Pub
from .serializers import  CategorySerializer, LogoSerializer, MessageListSerializer, MessageSerializer, OrderSerializer, OrderedProductSerializer, ProductImageSerializer,ProductSerializer, PubSerializer



class PubViewSet(viewsets.ModelViewSet):
    
    queryset = Pub.objects.all()
    serializer_class = PubSerializer



class ProductImageViewSet(viewsets.ModelViewSet):
    
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductGalleryViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LogoViewSet(viewsets.ModelViewSet):
    
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class SendMessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SendMessageListViewSet(viewsets.ModelViewSet):

    queryset = MessageList.objects.all()
    serializer_class = MessageListSerializer

from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        # Manually handle the creation of OrderedProduct instances
        for product_data in request.data.get('products', []):
            OrderedProduct.objects.create(
                order=order,
                product_id=product_data['product'],
                quantity=product_data['quantity'],
                taille=product_data.get('taille', 'L')
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderedProductViewSet(viewsets.ModelViewSet):
    queryset = OrderedProduct.objects.all()
    serializer_class = OrderedProductSerializer