from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import * 
from . serializer import *
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin,ListModelMixin
# Create your views here.


class BannerViewSet(ModelViewSet):
    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated]
    queryset =Banner.objects.all()
    serializer_class = BannerTopSerializer


class CategoryViewSet(ModelViewSet):
    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class ProductViewSet(ModelViewSet):
    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class CartViewSet(CreateModelMixin,GenericViewSet,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin,ListModelMixin):
    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated]
    # queryset = Cart.objects.prefetch_related('items__product').all()
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated]

    http_method_names=['get','post','patch','delete']
    def get_serializer_class(self):
        if self.request.method=='POST':
            return AddCartSerializer

        elif self.request.method=='PATCH':
            return UpdateCartItemSerializer 

        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id =self.kwargs['cart_pk'])