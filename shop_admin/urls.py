from django.urls import path
from . import views

# URL patterns for authentication and home page
urlpatterns = [
    path('', views.home,name="home"),               # Home page
    path('signup/',views.signup,name="signup"),     # User registration page
    path('signin/',views.signin,name="signin"),     # User login page
    path('logout/',views.signout,name="logout"),     # User logout action
    
    path('categories/',views.categories,name="categories"),
    path('categories_manage/',views.categories_manage,name='categories_manage'),
    path('categories_manage/<int:category_id>/',views.edit_category,name='edit_category'),
    path('category_create/',views.category_create,name='category_create'), # URL pattern for creating a new product category
    path('categories/<int:category_id>/',views.products_by_category,name='products_by_category'),

    path('product_create/',views.product_create,name='product_create'),
    path('edit_product/<int:product_id>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:product_id>/',views.delete_product,name='delete_product')
]