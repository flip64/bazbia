from django.shortcuts import render , redirect
from shop.models import Category,CateL1,CateL2,Slide,Daste,Collection,Product,DasteProduct,exeleFile
from customer.models  import Faktor, ProductFaktor , ListState
from account.views import accesspage
from config.baseClass import DasteBytedad , productByData 

'''
def index(request) :

  if not accesspage(request):
     return redirect('user_login')  
  
  
  
  catlist =  Category.objects.all()
  listL1 =CateL1.objects.all()
  listL2 =CateL2.objects.all()
  list_slide = Slide.objects.all()
  list_dasteh = Daste.objects.all()
  list_colection = Collection.objects.all()
  list_pruduct = Product.objects.all()


  listdastehbytedad = []   
  for l in list_dasteh:
     ld = DasteBytedad(l,len(DasteProduct.objects.filter(daste = l)))
     
     listdastehbytedad.append(ld)


  
  listPrudoct_bydata =[] 
  for l in list_pruduct:
     takhfif = l.takhfif/100
     temp = productByData(l , takhfif=int(l.price -  l.price * takhfif))  
     listPrudoct_bydata.append(temp)

  listpishnadi = Product.objects.all()   
  namedasteh = 'لیست محصولات'
  context= {
        'catlist'      : catlist,
        'listL1'       : listL1,
        'listL2'       : listL2,
        'listslid'     : list_slide,
        'listDasteh'   : listdastehbytedad,
        'listcolection': list_colection , 
        'listpruduct'  : listPrudoct_bydata,
        'listpishnadi' : listpishnadi,
        'namedasteh'   : namedasteh 
    }

  return render(request , 'shop/index.html' ,context) 


'''



def list_product(request):
 
  file = exeleFile.objects.get()
  print(file.file.url)


  catlist =  Category.objects.all()
  listL1 =CateL1.objects.all()
  listL2 =CateL2.objects.all()
  list_slide = Slide.objects.all()
  list_dasteh = Daste.objects.all()
  list_colection = Collection.objects.all()
  

  
##############3 LIST DASTEH 
  listdastehbytedad = []   
  for l in list_dasteh:
     ld = DasteBytedad(l,len(DasteProduct.objects.filter(daste = l)))
     listdastehbytedad.append(ld)




#####################3 LIST PRODUCT
  try:
   if (request.GET['daste']):
     nameDasteh =request.GET['daste']
     daste = Daste.objects.get(name=nameDasteh)
     if daste:
      list_product = DasteProduct.objects.filter(daste=daste)

  except:    
     list_product = Product.objects.all() 
     nameDasteh = 'جدید ترین محصولات'
    
    
#######  شمارش تعداد محصولات داخل سبد خرید   
  try : 
    member = request.user.member
    state = ListState.objects.get(englishName = 'sabad')
    faktor = Faktor.objects.get(member = member , state =state)
    listPrudoctSabad = ProductFaktor.objects.filter(faktor = faktor)
    tedadSaba = len(listPrudoctSabad)
  except : 
    tedadSaba =  0
    pass   




  context= {
        'catlist'      : catlist,
        'listL1'       : listL1,
        'listL2'       : listL2,
        'listslid'     : list_slide,
        'listDasteh'   : listdastehbytedad,
        'listcolection': list_colection , 
        'listpruduct'  : list_product,
        'namedasteh'   : nameDasteh    ,
        'tedadSabad'   : tedadSaba   ## تعداد محصولات داخل سبد خرید  
      }

  return render(request , 'shop/list_product.html' ,context) 
  
