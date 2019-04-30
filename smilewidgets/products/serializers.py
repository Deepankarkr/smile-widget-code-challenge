from rest_framework import serializers
from .models import ProductPrice,Product,GiftCard


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name','code','price',)

class prodpriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = ('Product', 'Amount', 'date_start', 'date_end', 'Schedule_name',)

class giftcardSerializer(serializers.ModelSerializer):

    class Meta:
        model = GiftCard
        fields = ('code', 'amount', 'date_start', 'date_end',)