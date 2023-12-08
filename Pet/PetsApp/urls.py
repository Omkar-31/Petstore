from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', PetList.as_view(),name="index"),
    path('petinfo', views.petinfo),
    # path('petinfo/<slug:slug>', PetDetail.as_view(),name="petdetail"),
    path('search', views.search),
    path('signup', views.signup),
    path('login',views.login),
    path('logout',views.logout_user),
    path('profile',views.UserProfile),
    path('addToCart',views.addToCart),
    path('removecart',views.removeCartItem),
    path('cartquantity',views.cartQuantity),
    path('mycart',views.viewCart),
    path('order',views.addOrder),
    path('payment',views.payment),
]
