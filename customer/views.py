from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect ,HttpResponse
from jalali_date import jdatetime
from shop.models import Product
from customer.models import Member ,ProductFaktor , Faktor ,ListState , Takhfif, Aqhsat,DafterAqhsat
from datetime import datetime
from account.views import accesspage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from config.config import *
from config.baseClass import *
from cart.utils.cart import Cart 





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

  
@login_required
def order(request) : 
   
   cart = Cart(request)   
   curentmember = request.user.member           ## عضوی که لاگین کرده 
   try: 
    takhfif = Takhfif.objects.get(code = request.session['takhfif'])
   except:
    takhfif = None 


   
   state = ListState.objects.get(englishName = 'order')        # فاکتور در حالت  سفارش 

   faktor = Faktor.objects.filter(member = curentmember, state = state)
   if len(faktor) != 0 : 
    messages.add_message(request ,messages.ERROR , "  کاربر سفارش فعال دارد  حذف شد   " )
    faktor.delete()
    return redirect ('cart:show_cart')
   else : 
     faktor = Faktor.objects.create(
       member = curentmember,
       state = state,
       sum = cart.get_total_price(),
       pardakht = 0 ,
       takhfif =takhfif 
     ) 

   faktor = Faktor.objects.get(member = curentmember, state = state)

   for item in cart: 
     ProductFaktor.objects.create(
       product= item['product'],
       faktor = faktor , 
       tedad = item['quantity'],

     )
  
   
   kol = request.POST['mablagh']
      

   context = {
    'member' : curentmember,
    'listproduc' : cart ,
    'kol'  : kol
   } 
   return  render(request , 'customer/pardakht.html' , context)


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
    return HttpResponseRedirect('/customer/taidePardakhtEtebari/?pardakhti='+ str(mablaghPardakhti)+ "&aghsat=" + str(mablaghAgsat) )
 except :
   messages.add_message(request, messages.INFO, "   بزای پرداخت اعتباری لطفا تیک تایید را بزنید      ")
   return HttpResponseRedirect('/customer/pardakht_etbari/?mablagh='+ str(mablagh))
    
 
#             تایید پرداخت نقدی
def taidePardakhtNaghdi(request): 
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

      ### تغیر حالت فاکتور از سفارش به حالت پرداخت شده  
      stateorder = ListState.objects.get(englishName = 'order')
      faktor = Faktor.objects.get(member = member , state = stateorder)
      statepardakht = ListState.objects.get(englishName = 'payed')
      faktor.state=statepardakht 
      faktor.save()

      ### خالی کردن سبد خرید 
      cart = Cart(request) 
      cart.clear()

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
     stateSabad = ListState.objects.get(englishName = 'order')
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
        
     ## تغیر وضعیت فاکتور به حالت در حال پرداخت 
     state_darhal_pardakht = ListState.objects.get(englishName = 'paying')
     faktor.state = state_darhal_pardakht  
     
     cart = Cart(request)
     cart.clear()

     if mablaghpardakhti != 0 :
        return HttpResponse('    پرداخت شد  ') 

     else :
      return HttpResponse('تمام مبلغ قسط بندی شد ') 
   





