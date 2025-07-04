from django.urls import path
from . import views

# URL patterns for authentication and home page
urlpatterns = [
    path('', views.home,name="home"),               # Home page
    path('signup/',views.signup,name="signup"),     # User registration page
    path('signin/',views.signin,name="signin"),     # User login page
    path('logout/',views.signout,name="logout"),     # User logout action
    
    path('categories_manage/',views.categories_manage,name='categories_manage'),
    path('categories_manage/<int:category_id>/',views.edit_category,name='edit_category'),
    path('delete_category/<int:category_id>/',views.delete_category,name='delete_category'),
    path('category_create/',views.category_create,name='category_create'), # URL pattern for creating a new product category

    path('all_products/',views.all_products,name='all_products'),
    path('product_create/',views.product_create,name='product_create'),
    path('edit_product/<int:product_id>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:product_id>/',views.delete_product,name='delete_product')
]