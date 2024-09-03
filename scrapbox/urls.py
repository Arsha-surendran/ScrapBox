"""
URL configuration for scrapbox project.

The urlpatterns list routes URLs to views. For more information please see:
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
from scrap import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegistrationView.as_view(),name="register"),
    path('signin/',views.LoginView.as_view(),name="signin"),
    path("logout/",views.SignOutView.as_view(),name="logout"),
    path("productadd/",views.ProductAddView.as_view(),name="productadd"),
    path("",views.IndexView.as_view(),name="home"),
    path("category/",views.CategoryAddView.as_view(),name="category"),
    path("productlist/",views.ProductListView.as_view(),name="product_list"),
    path("productedit/<int:pk>/change/",views.ProductUpdateView.as_view(),name="product_edit"),
    path("productdelete/<int:pk>/remove/",views.ProductDeleteView.as_view(),name="delete"),
    path("productdetail/<int:pk>/detail/",views.ProductDetailView.as_view(),name="product_details"),
    path("userprofile/<int:pk>/change/",views.ProfileUpdateView.as_view(),name="profile_edit"),
    path("profiledetail/<int:pk>/detail",views.ProfileDetailView.as_view(),name="profiledetail"),
    path("buy/<int:pk>/buy/",views.BuyView.as_view(),name="buy"),
    path("pay/",views.PayView.as_view(),name="pay"),
    path("product/<int:pk>/wishlist/",views.WishlistAddView.as_view(),name="wishlist"),
    path("product/wishlist/list",views.WishlistView.as_view(),name="wishlistdetail"),
    path('buy/payment',views.PaymentdetailView.as_view(),name="paym"),
    path("payment/",views.PaymentView.as_view(),name="payment")

    # path("wishlist/",views.WishlistView.as_view(),name="wishlist")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)