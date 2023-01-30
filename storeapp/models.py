from django.db import models
from decimal import Decimal
from uuid import uuid4
from django.core.validators import MinValueValidator

# Create your models here.



class Banner(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='banner_images',blank=True,null=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='categoty_images',blank=True,null=True)


    def __str__(self) -> str:
        return self.name

class Product(models.Model):

    UNIT_GRAM = 'g'
    UNIT_KILOGRAM = 'kg'
    UNIT_NOS = 'Nos'
    UNIT_LITER='Ltr'

    UNIT_CHOICES = [

        (UNIT_GRAM, 'Gram'),(UNIT_KILOGRAM,'Kilogram'),(UNIT_NOS,'Nos'),(UNIT_LITER,'Ltr')

    ]

    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='product_images',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6,decimal_places=2,default=Decimal(0))
    offer= models.IntegerField()
    unit =models.CharField(choices=UNIT_CHOICES,max_length=3)
    last_update=models.DateField(auto_now_add=True)

    def _get_offer_price(self):
        final=self.price * int(self.offer)/ Decimal(100)
        offer_price=self. price - final
        return offer_price
    offer_price=property(_get_offer_price)


    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)]) 


    class Meta:
        unique_together = [['cart','product']]


    