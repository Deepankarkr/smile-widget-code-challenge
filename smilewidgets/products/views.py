import json
from datetime import datetime
from rest_framework import generics
from .models import Product,GiftCard,ProductPrice
from .serializers import productSerializer,giftcardSerializer,prodpriceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


def sch_price(productcode,current_date):
    a=ProductPrice.objects.filter(Product=productcode)
    for i in a:
        if(str(i.date_end) !="None"):
            print(type(i.date_end))
            if(i.date_end>= current_date and i.date_start <= current_date ):
                return i.Amount
        elif(str(i.date_end) =="None"):
            if(i.date_start >= current_date):
                b=Product.objects.filter(pk=productcode)
                return [j.price for j in b][0]
            else:
                return i.Amount




def giftcard_off(giftcode,current_date):
    off_amount=0
    if(str(giftcode)!="None"):
        start_date = [a.date_start for a in GiftCard.objects.filter(code=giftcode)][0]
        date_end = [a.date_end for a in GiftCard.objects.filter(code=giftcode)][0]

        if(current_date>=start_date):
            if(giftcode.upper()=='250OFF'):
                off_amount=[a.amount for a in GiftCard.objects.filter(code='250OFF')][0]/100
            elif(giftcode.upper()=='50OFF'):
                off_amount = [a.amount for a in GiftCard.objects.filter(code='50OFF')][0]/100
            elif(giftcode.upper()=='10OFF'):
                off_amount = [a.amount for a in GiftCard.objects.filter(code='10OFF')][0]/100
            else:
                off_amount=0
        else:
            off_amount=0
    return off_amount


class enquiryList(generics.ListCreateAPIView):
    queryset = GiftCard.objects.all()
    serializer_class = giftcardSerializer


class enquiryDetail(APIView):
    def get(self, request, productcode,date,giftCardCode='None'):
        dt = datetime.strptime(date, '%Y-%m-%d').date()
        gift_off=giftcard_off(giftCardCode,dt)
        sch_p=sch_price(int(productcode),dt)
        res=sch_p-gift_off
        result = res if (res >=0) else 0
        x = { "Date" :dt ,"Product Code": productcode,"Gift Code": giftCardCode,"Amount": result}
        return Response(x)
