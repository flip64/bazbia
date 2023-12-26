from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('reducenumber/<product_id>' , views.reduce_number_from_cart , name = 'reduce_number_from_cart'),
    path('list/', views.show_cart, name='show_cart'),
    path('codeTkhfif/',views.codeTakhfif , name='codeTakhfif'),
    path('deletTkhfif/',views.deletTakhfif , name='delet_takhfif'),

]