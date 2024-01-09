from django.shortcuts import render , redirect
from shop.models import Category,Slide,Daste,Collection,Product
from customer.models  import Faktor, ProductFaktor , ListState
from account.views import accesspage
from config.baseClass import DasteBytedad , productByData 
from cart.utils.cart import Cart

def list_product(request):
 
  

  catlist =  Category.objects.all()
  list_slide = Slide.objects.all()
  list_dasteh = Daste.objects.all()
  list_colection = Collection.objects.all()
  

  
##############3 LIST DASTEH 
  listdastehbytedad = []   
  for l in list_dasteh:
     ld = DasteBytedad(l,len(Product.objects.filter(dasteh = l)))
     listdastehbytedad.append(ld)




#####################3 LIST PRODUCT
  try:
   if (request.GET['daste']):
     dasteh = Daste.objects.get(enghlishNmae=request.GET['daste'])
     if dasteh:
      list_product = Product.objects.filter(dasteh = dasteh)
      nameDasteh = dasteh.name
  except:    
     list_product = Product.objects.all() 
     nameDasteh = 'جدید ترین محصولات'
    
    
#######  شمارش تعداد محصولات داخل سبد خرید 
  cart = Cart(request)     
  tedadSaba =  len(cart.cart)
  
  context= {
        'catlist'      : catlist,
        'listslid'     : list_slide,
        'listDasteh'   : listdastehbytedad,
        'listcolection': list_colection , 
        'listpruduct'  : list_product,
        'namedasteh'   : nameDasteh    ,
        'tedadSabad'   : tedadSaba   ## تعداد محصولات داخل سبد خرید  
      }

  return render(request , 'shop/list_product.html' ,context) 
  
