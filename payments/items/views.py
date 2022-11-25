import stripe
from django.shortcuts import render, redirect
from .models import Item
from django.conf import settings


def item_detail(request, item_id):
    """
    View-функция, которая отображает
    информацию о тестовой вещи.
    """
    item = Item.objects.get(pk=item_id)
    return render(request, 'index.html', {'item': item})


stripe.api_key = settings.STRIPE_SECRET_KEY


def buy(request, item_id):
    """
    View-функция, которая создает форму для оплаты товара
    с помощью сервиса Stripe.
    """
    item = Item.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/pay_success',
        cancel_url='http://localhost:8000/pay_cancel',
    )
    return redirect(session.url, code=303)


def pay_success(request):
    """
    View-функция для отображения
    успешной оплаты.
    """
    return render(request, 'success.html')


def pay_cancel(request):
    """
    View-функция для отображения
    отмены платежа.
    """
    return render(request, 'cancel.html')
