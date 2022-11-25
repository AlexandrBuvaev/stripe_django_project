from django.urls import path
from . import views


urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('buy/<int:item_id>/', views.buy, name='buy'),
    path('pay_success/', views.pay_success, name='pay_success'),
    path('pay_cancel/', views.pay_cancel, name='pay_cancel'),
]
