from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_sale,name='create_sale'),
    path('search/', views.product_search, name='product_search'),
]



