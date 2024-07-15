from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .cart import Cart
from store.models import Product
from django.http import JsonResponse,HttpResponseBadRequest

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, 'cart_summary.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals})


def cart_add(request):
    cart = Cart(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = len(cart)
        messages.success(request, ('The product was added to cart'))
        return JsonResponse({'qty': cart_quantity})

    else:
        return HttpResponseBadRequest("Invalid request")



def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        # Call Delete Function in Cart
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request, ('Item deleted from cart!!'))
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
    
    cart.update(product=product_id, quantity=product_qty)

    response = JsonResponse({'qty':product_qty})
    messages.success(request, ('The cart has been updated!!'))
    return response