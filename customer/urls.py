from django.urls import path 
from customer import views 
urlpatterns = [
    path('', views.listMember ,name='listmember'),
    path('profile/', views.profile , name= 'profile'),
    path('addsabad/' , views.addsabad,name='addSabad'),
    path('removeSabad/' , views.removeSabad,name='removeSabad'),
    path('sabad/', views.listsabad, name="listSabad"),
    path('pardakht/' , views.pardakht, name = 'pardakht'),
    path('codeTkhfif/',views.codeTakhfif , name='codeTakhfif'),
    path('deletTkhfif/',views.deletTakhfif , name='deletTakhfif'),
    path('pardakht_naghdi/',views.pardakht_naghdi , name='pardakht_naghdi'),
    path('pardakht_etbari/',views.pardakht_etbari , name='pardakht_etbari'),
    path('taidePardakhtNaghdi/',views.taidePardakhtNaghdi ,name="taidePardakhtNaghdi"),
    path('taidePardakhtEtebari/',views.taidePardakhtEtebari ,name="taidePardakhtEtebari"),
    
    


]