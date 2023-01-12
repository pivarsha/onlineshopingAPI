from django.urls import path,include
from .views import *

urlpatterns = [
    


path("categories",ListCategory.as_view(),name="categorie"),
path("categories/<int:pk>/",DetailCategory.as_view(),name="singlecategory"),

path("book",ListBook.as_view(),name="books"),
path("books/<int:pk>/",DetailBook.as_view(),name="singlebook"),

path("products",ListProduct.as_view(),name="Product"),
path("products/<int:pk>/",DetailProduct.as_view(),name="singleProducts"),

path('users',ListUser.as_view(),name="users"),
path('singleusers/<int:pk>/',DetailUser.as_view(),name="singleusers"),

path('carts',ListCart.as_view(),name="allcarts"),
path('carts/<int:pk>/',DetailCart.as_view(),name="detailcarts"),

]