from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.core.validators import MaxValueValidator, MinValueValidator
from shop.models import Product 
from account.models import Role
# Create your models here.



class Level(models.Model):
    name = models.CharField(max_length=150)
    englishName = models.CharField(max_length=150)
    maxMablagh = models.BigIntegerField()
    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    level = models.ForeignKey(Level , on_delete=models.DO_NOTHING ,null=True)
    etebar = models.BigIntegerField(null=True,blank=True)     #  اعتبار باقی مانده
    role = models.ForeignKey(Role , on_delete= models.DO_NOTHING , default= None , null=True)
    
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

###  لیست وضعیتهای  فاکتور 
class ListState(models.Model): 
  name = models.CharField(max_length= 200 , null= True)
  englishName = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name

#### تخفیفات
class Takhfif(models.Model):
    name= models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    darsad = models.FloatField(default=0 , validators=[
        MinValueValidator(0),
        MaxValueValidator(1)])    
    maximum = models.BigIntegerField(default= 0 )  #          ماکسیموم تخفیف 
    expierDate = jmodels.jDateField()
    state = models.BooleanField(default=True)
    
    def __str__(self) :
        return self.name



##  فاکتور
class Faktor(models.Model): 
  member = models.ForeignKey(Member , on_delete=models.CASCADE , blank= True , null= True)
  date = jmodels.jDateTimeField(auto_now=True)
  state = models.ForeignKey(ListState ,on_delete= models.DO_NOTHING , null=True )
  sum = models.BigIntegerField(default= 0)              ##  جمع کل فاکتور 
  pardakht = models.BigIntegerField(default=0 , null= True , blank= True)          ##  پرداختی فاکتور
  takhfif = models.ForeignKey(Takhfif , on_delete= models.DO_NOTHING , null= True , blank=True)
  def __str__(self):
      return self.member.__str__()      
  
#  دفتر اقساط مربوط به فاکتور   
class DafterAqhsat(models.Model):
    faktor = models.ForeignKey(Faktor , on_delete=models.CASCADE , null=True ,blank= True)
    mablagh  =  models.BigIntegerField()     #   مبلغ کل بدهی
    tedad   = models.IntegerField()          #   تعداد اقساط
    def __str__(self) :
        return  ' daftar  ' + self.faktor.__str__()




 # اقساط مربوط به دفتر اقساط

class Aqhsat(models.Model):
    aghsat= models.ForeignKey(DafterAqhsat ,on_delete=models.CASCADE, null=True , blank=True ) 
    tarikhSarresid = jmodels.jDateField()
    tarikhPardakht = jmodels.jDateField(null=True,blank=True)
    mablagh = models.BigIntegerField()          #  مبلغ هر قسط 
    namber = models.IntegerField()
    def __str__(self):
        return 'qhest no ' + str(self.namber) + ' ' + self.aghsat.__str__()


###  لیست محصولات داخل فاکتور 
class ProductFaktor(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE , null= True , blank=True)
    faktor = models.ForeignKey(Faktor , on_delete= models.CASCADE , null = True , blank=True)        
    tedad = models.IntegerField(default=1)   
    def __str__(self):
       return  self.product.name + "  for " + self.faktor.__str__()

    

