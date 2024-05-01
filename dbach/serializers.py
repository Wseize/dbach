from rest_framework import serializers
from .models import Category, Logo, Message, MessageList, Order, OrderedProduct, Product, ProductImage, Pub


class PubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pub
        fields = ['id', 'name', 'image']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'choice', 'choice_type', 'quantity', 'images']



class CategorySerializer(serializers.ModelSerializer):
    products= ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image','products']

class MessageSerializer(serializers.ModelSerializer):
    gallery_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'username', 'email', 'mobile','adress' , 'image','xposition_image','yposition_image','text_added','text_size', 'text_font_family', 'xposition_text','yposition_text', 'gallery', 'gallery_name', 'taille', 'date_sent']

    def get_gallery_name(self, obj):
        if obj.gallery:
            return obj.gallery.name
        return None
    

class MessageListSerializer(serializers.ModelSerializer):
    gallery_names = serializers.SerializerMethodField()

    class Meta:
        model = MessageList
        fields = ['id', 'username', 'email', 'mobile', 'galleries', 'gallery_names', 'taille', 'date_sent']

    def get_gallery_names(self, obj):
        return [gallery.name for gallery in obj.galleries.all()]


class LogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logo
        fields = ['id', 'name', 'image']




class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'date_ordered', 'sender_name', 'sender_mobile','sender_email','sender_adress','total_price', 'products']

    def get_products(self, obj):
        ordered_products = OrderedProduct.objects.filter(order=obj)
        product_data = [{'id': ordered_product.product.id,'product_name': ordered_product.product.name,  'quantity': ordered_product.quantity, 'taille': ordered_product.taille} for ordered_product in ordered_products]
        return product_data
        

class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = '__all__'






