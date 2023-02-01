from django.contrib import admin
from . models import *
from . import models

# Register your models here.


admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display =['id','full_name','mobile_number','pincode','town','street','land_mark']