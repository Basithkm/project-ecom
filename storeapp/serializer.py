from rest_framework import serializers
from .models import *
from decimal import Decimal



class BannerTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','name','image']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','image']



class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source ='category.name',read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','image','category','price','offer_price','offer','unit','category_name','last_update']
    offer_price = serializers.SerializerMethodField(method_name='calculate_final_price')
    
    def calculate_final_price(self,product:Product):
        final= product.price * int(product.offer)/ Decimal(100)
        return product.price - final


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','offer','offer_price']

    offer_price = serializers.SerializerMethodField(method_name='calculate_final_price')

    def calculate_final_price(self,product:Product):
        final= product.price * int(product.offer)/ Decimal(100)
        return product.price - final

class CartItemSerializer(serializers.ModelSerializer):
    product =  SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self,cart_item:CartItem):
        return cart_item.quantity * cart_item.product.price
        
    class Meta:
        model=CartItem
        fields = ['id','product','quantity','total_price']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many=True,read_only=True)

    total_price = serializers.SerializerMethodField()

    def get_total_price(self,cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])

    class Meta:
        model = Cart
        fields = ['id','items','total_price']


class AddCartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self,value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No product with given ID was found.')
        return value 


    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id,product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id,**self._validated_data)
        
        return self.instance

    class Meta:
        model = CartItem
        fields =['id','product_id','quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']