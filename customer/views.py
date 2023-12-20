from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect ,HttpResponse
from jalali_date import jdatetime
from shop.models import Product,exeleFile
from customer.models import Member ,ProductFaktor , Faktor ,ListState , Takhfif, Aqhsat,DafterAqhsat
from datetime import datetime
from account.views import accesspage
from django.contrib import messages
from config.config import *
from config.baseClass import *






# Create your views here.
def listMember(request): 
   if not accesspage(request):
     return redirect('user_login')
  

   listMember = Member.objects.all()
   context = {
      'listmember' : listMember,
   }   
   return render (request , 'customer/list_members.html' ,context )




def profile(requset): 
   if not accesspage(requset):
     return redirect('user_login')
  
   context=  {
    }
   return render(requset , 'profile.html',context)


def addsabad(requset):
    ###  اضافه کردن یک محصول به داخل سبد خرید 
    curentmember = requset.user.member           ## عضوی که لاگین کرده 
    id = int(requset.GET['id'])
    product = Product.objects.get(pk = id)                 #  محصولی که می خواهیم به سبد خرید اضافه کنیم 
    state = ListState.objects.get(englishName = 'sabad')        # فاکتور در حالت سبد خرید 
    date = jdatetime.datetime.now()
    
    
    # فاکتور های کاربر که وضعیت آن در حالت سبد خرید باشد را بر میگردانیم و در صورت نبود ایجاد میکنیم   
    try :  
      faktor = Faktor.objects.get(member = curentmember, state = state)
    except:    
       faktor = Faktor.objects.create(
       member = curentmember ,
       date = date , 
       state =  state,
       pardakht = 0 ,
       takhfif = None  ,
       sum = 0     ) 

     


    #   محصول را به لیست فاکتوراضافه میکنیم اگر از قبل موجود باشد به تعداد آن آضافه میکنیم           
    

     # to do لیست انبار باید چک شود 
    try :
      productFaktor = ProductFaktor.objects.get(product = product , faktor = faktor)
      productFaktor.tedad = productFaktor.tedad +1 
      productFaktor.save()
      faktor.sum = faktor.sum + product.price
      faktor.save()
    except :  
     ProductFaktor.objects.create(
      faktor = faktor ,
      product = product ,
      tedad = 1 , 
     )
     ##      قیمت محصول اضافه شده به فاکتور را در جمع فاکتور اضافه میکند 
     faktor.sum = faktor.sum + product.price 
     faktor.save()
     

   
    # لیست سبد خرید را فراخوانی میکنیم 
    return redirect('/customer/sabad?id='+str(curentmember.pk))



def removeSabad(requset): 
    ########## برای حذف یک محصول از داخل سبد خرید 

    # کاربری که لاگین کرده 
    curentmember = requset.user.member                       

    # استخراج محصول از دیتابیس با استفاده از ایدی محصول 
    id = int(requset.GET['id'])
    product = Product.objects.get(pk = id)
    
    
    state = ListState.objects.get(englishName = 'sabad')
    # استخارج فاکتور مربوط به کاربر از دیتابیس

    try:
     faktor  = Faktor.objects.get(member = curentmember ,  state =state ) 
    except : 
      return redirect('/customer/sabad?id='+str(curentmember.pk))

    # چک میکنیم که آبا محصول از قبل در سبد خرید بوده یا نه 
    try:   
       productFactor  = ProductFaktor.objects.get(product = product ,faktor = faktor)
       #  اگر تعداد محصول فقط یک عدد باشد  محصول را از سبد حذف میکنیم 
       if (productFactor.tedad <= 1  ):
          productFactor.delete()
       else :   
        #  اگر تعداد محصول بیشتر از یک باشد یک واحد از تعداد آن کم می کنیم 
        productFactor.tedad = productFactor.tedad -1 
        faktor.sum = faktor.sum -product.price
        productFactor.save()
        faktor.save()
    except :   
       return redirect('/customer/sabad?id='+str(curentmember.pk))
    
    
    
    pr = ProductFaktor.objects.filter(faktor =faktor) 
    if(len(pr) == 0):  
     faktor.delete()




    return redirect('/customer/sabad?id='+str(curentmember.pk))
    
     
    # اگر محصول در  سبد نبود فاکتور را حدف مکنیم و به صفحه سبد خرید باز میگردیم  
      



def listsabad(request) :
  # برای محصولات وپارامتر های اضافه آن  کلاس ایجاد میکنیم 
  class sabadpru:
     def __init__(self,product,tedad,jame) :
        self.product =product
        self.tedad =tedad
        self.jame =jame
        
  memberId = int(request.GET['id'])           
  user  = User.objects.get(pk = memberId)
  member = Member.objects.get(user = user)
   # چک میکنیم وضعیت در حالت سبد خرید باشد 
  try:
    state = ListState.objects.get(englishName= 'sabad' ) 
  except:  
    state = None
    print("not sabad state ")
  
  try:       # چک کردن سبد خرید کاربر 
    faktor = Faktor.objects.get(member = member , state=state)
  except: 
        messages.add_message(request, messages.INFO, "  سبد خرید خالی است   " , extra_tags="danger")
        return redirect ("/shop")
      
    
  listpruductSabad = ProductFaktor.objects.filter(faktor=faktor)
  listproduct =  [] 
  hamlonaghl = 50000
  for l in listpruductSabad :
      tedad = l.tedad
      jame = l.tedad * l.product.takhfif       
      s =sabadpru(l.product,tedad,jame)
      listproduct.append(s) 


  # بررسی  میزان تخفیف فاکتور 
  # محدودیت تخفیف با فیلد maximum
  # اگر برابر با  -1 باشد تخفیف نا محدود است 

  jamekol = faktor.sum
  if (faktor.takhfif):
    takhfif = int(jamekol * faktor.takhfif.darsad)
    if faktor.takhfif.maximum != -1 : 
     if(takhfif > faktor.takhfif.maximum): 
      takhfif = faktor.takhfif.maximum
  else :
    takhfif = 0 

  kol = jamekol + hamlonaghl - takhfif 


                    ##  ارسال  لیست محصولات سبد خرید
                    
  context = {
      'listprudoct' : listproduct,
      'id' : id,  # ایدی کاربر  
      'alljame': faktor.sum,
      'hamlonaghl' : hamlonaghl,
      'kol':kol,
      'takhfif' : takhfif,

     }
  return render(request, 'customer/list_sabad.html' ,context)
  
  
  

def pardakht(request) : 
   
   class productFacorCalss: 
     def __init__(self, product , tedad , jame ): 
       self.product = product
       self.tedad = tedad 
       self.jame = jame  
       
   
   
   curentmember = request.user.member           ## عضوی که لاگین کرده 
   state = ListState.objects.get(englishName = 'sabad')        # فاکتور در حالت سبد خرید 
    
    
    # فاکتور های کاربر که وضعیت آن در حالت سبد خرید باشد را بر میگردانیم         
   try :  
      faktor = Faktor.objects.get(member = curentmember, state = state)
   except:    
      messages.add_message(request ,messages.ERROR , "  سبد خالی  است " )
      redirect(request , "listSaba")

   listpruductFaktor = ProductFaktor.objects.filter(faktor=faktor)
   listproduct =  [] 
   for l in listpruductFaktor :
      tedad = l.tedad
      jame = l.tedad * l.product.price       
      s =productFacorCalss(l.product,tedad,jame)
      listproduct.append(s) 

   
   kol = request.POST['mablagh']
      

   context = {
    'member' : curentmember,
    'listproduc' : listproduct ,
    'kol'  : kol
   } 
   return  render(request , 'customer/pardakht.html' , context)

# بررسی کد تخفیف 
def codeTakhfif(request): 
    
   code = request.POST['code']
   try:  
         takhfif =  Takhfif.objects.get(code = code) 
         if(takhfif) : 
          member  = request.user.member
          try:  
           state = ListState.objects.get(englishName = 'sabad') 
          except : 
           messages.add_message(request, messages.INFO, " وضعیت سبد موجود نیست  ")

          try : 
           faktor = Faktor.objects.get(member=member , state = state)
          except : 
           print ("fakto mojod nist ")
           messages.add_message(request, messages.INFO, " سبد خرید موجود نیست     ")
        
          faktor.takhfif = takhfif
          faktor.save()
          messages.add_message(request, messages.INFO,  "  کد تخفیف  " + takhfif.name +  "  اعمال شد     "  , extra_tags= 'success')
         else : 
              messages.add_message(request, messages.INFO, " کد تخیف موجود نیست  " , extra_tags='warning')
   except: 
     messages.add_message(request, messages.INFO, " کد تخیف موجود نیست  " , extra_tags='warning') 





   return redirect('/customer/sabad?id='+str(request.user.member.pk))   


def deletTakhfif(request): 
   try: 
        member  = request.user.member
        try:  
          state = ListState.objects.get(englishName = 'sabad') 
        except : 
           print ( 'وضعیت سبد موجود نیست ')   
        try : 
         faktor = Faktor.objects.get(member=member , state = state)
        except : 
           print ("fakto mojod nist ")
        
        faktor.takhfif = None
        faktor.save()
        messages.add_message(request, messages.INFO, " کد تخفیف حذف شد     " , extra_tags='danger')


   except: 
    messages.add_message(request, messages.INFO, " کد موجود نیست  " , extra_tags= 'warning')

 
   return redirect('/customer/sabad?id='+str(request.user.member.pk))   


def pardakht_naghdi(request): 
  
  if request.method == "POST" : 
   mablagh = request.POST['mablagh'] 
  else:
    if request.method  == "GET" :
     if request.GET['mablagh'] == None:
       mablagh = 0 
     else: 
      mablagh = request.GET['mablagh'] 
    


  context={
    'mablagh' : mablagh ,
  }
  return render(request,'customer/pardakht_naghdi.html' , context)

def pardakht_etbari(request): 
 try:
  if request.GET['mablagh'] :   
    mablagh = int(request.GET['mablagh'])
 except : 
    mablagh = 0



   

 member = request.user.member 
 etebar = int(member.etebar)
 
    # شرایط پرداخت اعتباری 
    # 1 کاربر بدهکار نباشد 
    # 2 اعتبار کافی داشته باشد   

    #بررسی شرط بدهکاری کاربر 
 if bedehimember(member) != 0 : 
   messages.add_message(request, messages.INFO, " به علت پدهکاری امکان پرداخت اعتباری وجود ندارد")
   return HttpResponseRedirect('/customer/pardakht_naghdi/?mablagh='+ str(mablagh))


    #بررسی شرط داشتن اعتبار 
 else :
      if etebar == 0 :
        messages.add_message(request, messages.INFO, "   اعتبار شما صفر است  ")
        return HttpResponseRedirect('/customer/pardakht_naghdi/?mablagh='+ str(mablagh))
      


      mablaghPardakhti=0                         #  مبلغی که باید نقدی پرداخت شود 
      mablaghAgsat=0                              # مبلقی مه باید قسط بندی شود

      
      if etebar >= mablagh : 
        mablaghPardakhti = 0                     
        mablaghAgsat = etebar - mablagh          
      else: 
        mablaghPardakhti = mablagh - etebar
        mablaghAgsat = etebar  

     
 tAghst = tedadAghsat(mablaghAgsat)
 listaghsat = []
 date = jdatetime.date.today()
 for l in range(tAghst):
    date = next_month(date)
    aghsat = Aqhsat(
     
      mablagh= int(etebar / tAghst),
      namber=l+1,
      tarikhSarresid = date,
      )
    listaghsat.append(aghsat)

 
 if request.method == 'GET':   
    context = {
      'listaghsat'       : listaghsat,
      'etebrMember'      : etebar,
      'mablagh'          : mablagh ,
      'mablaghPardakhti' : mablaghPardakhti
     }
    return render(request , 'customer/pardakht_etebari.html' , context) 
 
 
 try:
  if request.method == 'POST':
   if request.POST['taid'] == 'ok':
    print(request.POST)
    return HttpResponseRedirect('/customer/taidePardakhtEtebari/?pardakhti='+ str(mablaghPardakhti)+ "&aghsat=" + str(mablaghAgsat) )
 except :
   messages.add_message(request, messages.INFO, "   بزای پرداخت اعتباری لطفا تیک تایید را بزنید      ")
   return HttpResponseRedirect('/customer/pardakht_etbari/?mablagh='+ str(mablagh))
    
 

   
#             تایید پرداخت نقدی
def taidePardakhtNaghdi(request): 
 print(request.method) 
 if request.method == "POST" : 
    '''
      شرایط اضافه کردن به اعتبار کاربر 
     1. کاربر بدهکار نباشد
     2.میزان اعتبار ان از سقف مجاز بیشتر نباشد

    '''     

    et = int(request.GET['mablagh'])* 0.01
  

    if request.POST['state'] == 'ok' :
      member = request.user.member      
      if(bedehimember(member)==0  ):
       member.etebar = member.etebar + et
       if member.etebar > member.level.maxMablagh:
        member.etebar = member.level.maxMablagh
       member.save()
      state = 'پرداخت شد '
    else: 
     state = 'پرداخت نشد' 
  
 context = {
    'state' : state 
  }    
      
 return render(request,'customer/taidepardakhtNaghdi.html' , context)



#             تایید پرداخت اعتباری
def taidePardakhtEtebari(request): 
     mablaghaghsat = int(request.GET['aghsat'])
     mablaghpardakhti = int(request.GET['pardakhti'])
     member = request.user.member 

     # ایجاد دفترچه اقساط 
     stateSabad = ListState.objects.get(englishName = 'sabad')
     faktor = Faktor.objects.get(member=member , state = stateSabad)
     tAghsat = tedadAghsat(mablaghaghsat)
     daftaraghsat = DafterAqhsat.objects.create(
       faktor =faktor, 
       mablagh = tAghsat , 
       tedad =tedadAghsat(mablaghaghsat))
     # ایجاد اقساط
     date = jdatetime.date.today()
     for li in range(tAghsat):
        date = next_month(date) 
        Aqhsat.objects.create(
          aghsat = daftaraghsat,
          tarikhSarresid = date,        
          tarikhPardakht = None,
          mablagh = int(mablaghaghsat/tAghsat),
          namber = li+1,
        )    
     messages.add_message(request ,messages.INFO,"دفترچه اقساط ایجاد شد " , )
     member.etebar = member.etebar - mablaghaghsat   
     member.save()
     if mablaghpardakhti != 0 :
      return HttpResponseRedirect('/customer/pardakht_naghdi/?mablagh='+ str(mablaghpardakhti))
     else :
      return HttpResponse('تمام مبلغ قسط بندی شد ') 
   





