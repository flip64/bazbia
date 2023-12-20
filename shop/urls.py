from django.urls import path 
from shop import views 
urlpatterns = [
    path('', views.list_product  , name = 'shopindex' ),
    path('listproduct/',views.list_product , name= 'list_product')
]