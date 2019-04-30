from django.contrib import admin
from .models import Product,GiftCard,ProductPrice

myModels = [Product,GiftCard,ProductPrice]  # iterable list
admin.site.register(myModels)