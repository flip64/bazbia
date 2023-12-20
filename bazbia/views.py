from django.shortcuts import render ,redirect
from config.baseClass import DasteBytedad,productByData,accesspage
from shop.models import Category ,CateL1,CateL2,Slide ,Daste,Collection,Product,DasteProduct 






def index(request): 
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



  return  render (request , 'index.html' , context)