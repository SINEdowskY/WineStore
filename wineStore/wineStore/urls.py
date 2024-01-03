"""
URL configuration for wineStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainPage, name="main"),
    #ACCOUNTS
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutView, name="logout"),
    path("account/", views.accountPage, name="account"),
    path("add/client/", views.addClientPage, name="add_client"),
    path("edit/client/<int:client_id>/", views.editClientPage, name="edit_client"),
    #WINEPAGES
    path("wine/<str:wine_type>/", views.winePage, name="wine_page"),
    path("wine/detail/<int:wine_id>/", views.detailWinePage),
    #CART
    path("cart/<int:wine_id>/", views.addToCartView, name="add_to_cart"),
    path("cart/", views.CartView, name="cart_view"),
    path("cart/decrement/<int:cart_item_id>/", views.decrementCartItem, name="decrement_item"),
    path("cart/increment/<int:cart_item_id>/", views.incrementCartItem, name="increment_item"),
    path("cart/remove/<int:cart_item_id>/", views.removeCartItem, name="remove_item"),
    #ORDER
    path("checkout/", views.CheckoutPage, name="checkout"),
    path("order/<int:order_id>/", views.detailOrderPage, name="detail_order")
]
