from django.shortcuts import render,redirect,get_object_or_404

from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def cart_details(request,tot=0,count=0,cart_items=None):

    try:
        ct = Cart.objects.get(cart_id=c_id(request))
        ct_items = Item.objects.filter(cart=ct, active=True)

        for i in ct_items:
            tot += (i.prodt.price*i.quantity)
            count += i.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key

    if not ct_id:
        ct_id = request.session.create()

    return ct_id


def add_cart(request, product_id):

    prod = Product.objects.get(id=product_id)

    try:
        ct = Cart.objects.get(cart_id=c_id(request))

    except Cart.DoesNotExist:
        ct = Cart.objects.create(cart_id=c_id(request))
        ct.save()

    try:
        c_items = Item.objects.get(prodt=prod, cart=ct)

        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity += 1
        c_items.save()

    except Item.DoesNotExist:
        c_items = Item.objects.create(prodt=prod, quantity=1, cart=ct)
        c_items.save()
        return redirect('cart')


def product_id(args):
    pass


def min_cart(request):
    ct = Cart.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Item.objects.get(prodt=prod, cart=ct)

    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()

    else:
        c_items.delete()
        return redirect('cart')


def cart_delete(request,product_id):
    ct = Cart.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Item.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cart')


