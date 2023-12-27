from django.urls import path 
from customer import views 
urlpatterns = [
    path('', views.listMember ,name='listmember'),
    path('profile/', views.profile , name= 'profile'),
    path('pardakht/' , views.order, name = 'pardakht'),
    path('pardakht_naghdi/',views.pardakht_naghdi , name='pardakht_naghdi'),
    path('pardakht_etbari/',views.pardakht_etbari , name='pardakht_etbari'),
    path('taidePardakhtNaghdi/',views.taidePardakhtNaghdi ,name="taidePardakhtNaghdi"),
    path('taidePardakhtEtebari/',views.taidePardakhtEtebari ,name="taidePardakhtEtebari"),
    
    


]