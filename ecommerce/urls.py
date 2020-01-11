from django.conf.urls import static
from django.urls import path

from .views import (
    HomeView,
    ItemDetailView,
    add_to_cart,
    CheckoutView,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView

)

app_name ='ecommerce'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('checkout/',CheckoutView.as_view(), name='checkout'),
    path('order-summary', OrderSummaryView.as_view(),name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<code>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-from-single-item-cart/<slug>/', remove_single_item_from_cart, name='remove-from-single-item-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon')
]