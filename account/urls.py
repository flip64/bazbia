from django.urls import path 
from account import views 
urlpatterns = [
       
   path('register/' , views.user_register , name= 'user_register'),
   path('userlogin/' , views.user_login , name= 'user_login'),
   path('userlogout/' , views.user_logout , name='userlogout'),
   path('pagelist/' ,views.pageList,name='pagelist' ),
   path('pagecreate/' ,views.pageCreate,name='pagecreate'),
   path('pageupdate/' ,views.pageUpdate,name='pageupdate'),
   path('accessList/' , views.accesslist , name = 'accessList'),
   path('rolelist/' , views.roleList , name = 'roleList'),
   path('order/' , views.upOrder ,name= 'uporder'),
 ##  path('/account/downorder/' , views.downOrder ,name= 'downorder'),
   path('addacess/' , views.addAcessview , name = 'addAcess'),
   path('removeaccess/' , views.removeAccessView , name = 'removeAccess'),



]