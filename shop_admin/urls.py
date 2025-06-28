from django.urls import path
from . import views

# URL patterns for authentication and home page
urlpatterns = [
    path('', views.home,name="home"),               # Home page
    path('signup/',views.signup,name="signup"),     # User registration page
    path('signin/',views.signin,name="signin"),     # User login page
    path('logout/',views.signout,name="logout"),     # User logout action
    path('category_create/',views.category_create,name='category_create'), # URL pattern for creating a new product category
    path('product_create/',views.product_create,name='product_create')
]