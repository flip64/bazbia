from django.contrib import admin
from shop.models import Category,Product,Daste,DasteProduct,Moshabe,Slide,Collection
from customer.models import Level,Member,DafterAqhsat,Aqhsat,Takhfif,Faktor,ListState,ProductFaktor
from account.models import PageCate,Page,AccessList,Role
# Register your models here.

###########3 shop
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Daste)
admin.site.register(DasteProduct)
admin.site.register(Moshabe)
admin.site.register(Slide)
admin.site.register(Collection)




############33  customer 
admin.site.register(Level)
admin.site.register(Member)
admin.site.register(DafterAqhsat)
admin.site.register(Aqhsat)
admin.site.register(Takhfif)
admin.site.register(Faktor)
admin.site.register(ListState)
admin.site.register(ProductFaktor)







####################  account 
admin.site.register(PageCate)
admin.site.register(Page)
admin.site.register(Role)
admin.site.register(AccessList)
