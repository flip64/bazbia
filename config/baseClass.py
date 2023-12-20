
from account.models import AccessList 
import calendar , datetime



class DasteBytedad:
     def __init__(self ,dasteh , tedad):
        self.dasteh = dasteh
        self.tedad = tedad



class productByData : 
     def __init__(self ,product , takhfif):
        self.product = product 
        self.takhfif = takhfif 



#                             توابع مورد نیاز قبل از راه اندازی سیستم 


## بررسی دستری به پیج مدیریت
def accessToModir(req):   
  if  not req.user.is_authenticated : 
   return False
  else : 
   role = req.user.member.role
   listacespage = AccessList.objects.filter(role = role)
   for list in listacespage : 
    if list.page.pageENnam == 'modir':
     return True   
  
  return False

## بررسی دستری به صفحه مورد نظر 
def accesspage(req):
  if  not req.user.is_authenticated : 
   return False
  else : 
   role = req.user.member.role
   listacespage = AccessList.objects.filter(role = role)
   for list in listacespage : 
       if list.page.url == req.path:
         return True   
  
  return False

## بررسی بدهکاری کاربر
def bedehimember(Member):
  return 0
  

## تعداد اقساط بر اساس مبلغ کا بدهیی و سطح کاربر تعیین می شود
def tedadAghsat(mablagh): 
  if mablagh == 0 : 
    return 0 
  if mablagh > 0 & mablagh <=500000: 
    return 1
  if mablagh > 50000 & mablagh <= 2000000 : 
    return 4
  if mablagh > 2000000 : 
    return 5
  

   
def next_month ( date ):
  """return a date one month in advance of 'date'.  
  If the next month has fewer days then the current date's month, this will return an
  early date in the following month."""
  return date + datetime.timedelta(days=calendar.monthrange(date.year,date.month)[1])

