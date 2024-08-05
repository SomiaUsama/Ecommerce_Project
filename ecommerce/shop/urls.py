from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name= 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('shop/add_category/', add_category, name='add_category'),
    path('shop/edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('shop/delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('shop/add_product/', add_product, name='add_product'),
    path('shop/edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('shop/delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
]

