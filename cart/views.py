from customer.models import Takhfif

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cart.utils.cart import Cart
from .forms import QuantityForm
from shop.models import Product


@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    messages.success(request, 'Added to your cart!', 'info')
    return redirect('cart:show_cart')


def show_cart(request):
    cart = Cart(request)
    hamlonaghl = 50000 
    codetakhfif = request.session.get("takhfif")
    try :
     takhfif = Takhfif.objects.get(code =  codetakhfif)
    except : 
       takhfif = None 

    # بررسی  میزان تخفیف فاکتور 
    # محدودیت تخفیف با فیلد maximum
    # اگر برابر با  -1 باشد تخفیف نا محدود است 

    jamekol = cart.get_total_price()
    if (takhfif):
      mtakhfif = int(jamekol * takhfif.darsad) 
      if takhfif.maximum != -1 : 
       if(mtakhfif > takhfif.maximum): 
        mtakhfif = takhfif.maximum
    else :
      mtakhfif = 0 

    kol = jamekol + hamlonaghl - mtakhfif 
  

    print(cart)
    context = {
        'cart': cart ,                                  #   لیست محصولات 
        'alljame': jamekol,                             #   جمع قیمت یدون محاسبه تخفیف
        'hamlonaghl' : hamlonaghl,                      #   هزینه حمل ونقل 
        'kol': kol,                                     #   جمع قیمت با محاسبه تخفیف 
        'takhfif' : mtakhfif,                           #   میزان تخفیف 
          
          
          
               }

    return render(request, 'cart/list_sabad.html', context)


@login_required
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:show_cart')


def reduce_number_from_cart(request , product_id): 
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)
    cart.reduceNumber(product)
    messages.success(request, 'remove  from your cart!', 'info')

    return redirect('cart:show_cart')



# بررسی کد تخفیف 
def codeTakhfif(request): 
    
   code = request.POST['code']
   try:  
         takhfif =  Takhfif.objects.get(code = code) 
         if(takhfif) : 
          request.session['takhfif'] = takhfif.code
          messages.add_message(request, messages.INFO,  "  کد تخفیف  " + takhfif.name +  "  اعمال شد     "  , extra_tags= 'success')
         else : 
              messages.add_message(request, messages.INFO, " کد تخیف موجود نیست  " , extra_tags='warning')
   except: 
     messages.add_message(request, messages.INFO, " کد تخیف موجود نیست  " , extra_tags='warning') 





   return redirect('cart:show_cart')   

# حذف کد تخفیف
def deletTakhfif(request): 
       
   del request.session['takhfif']
   messages.add_message(request, messages.INFO, " کد تخفیف حذف شد     " , extra_tags='danger')
   return redirect('cart:show_cart')   





