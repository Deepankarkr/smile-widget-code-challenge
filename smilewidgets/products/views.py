from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context,loader
from products.models import GiftCard,Product,ProductPrice

# Create your views here.
def index(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context,request))

def detail(request,path):
    l=path.split("_")
    productcode,Giftcardcode,date_str,=l[0],l[1],l[2]
    dic={"Big-Widget":1,"Small-Widget":2}
    date=datetime.strptime(date_str,'%Y-%m-%d').date()
    result=sch_price(dic[productcode],date)-giftcard_off(Giftcardcode,date)
    template = loader.get_template('index.html')

    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))


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
    if(str(giftcode)!=""):
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