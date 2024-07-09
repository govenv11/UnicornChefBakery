"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from enduser import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("/",views.index),
    path("",views.index),
    path("cart/",views.ShoppingCart),
    path("about/",views.about),
    path("contact/",views.contact),
    path("faq/",views.faq),
    path("privacypolicy/",views.privacypolicy),
    path("reviewsandnewsletter/",views.reviewsandnewsletter),
    path("termsandconditions/",views.termsandconditions),
    path("wishlist/",views.wishlist),
    path('products/', views.Products),
    path('checkout/', views.checkout),
    path("login/",views.login),
    path('order/', views.order,name='order'),    
    path('order/success/', views.ordercomplete,name='process_payment'),
    # path('customer/<int:customerno>/', views.customer, name='customer'),
    ]