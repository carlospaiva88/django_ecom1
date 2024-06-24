from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse,HttpResponseBadRequest

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {'cart_products':cart_products, 'quantities':quantities})


def cart_add(request):
    cart = Cart(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = len(cart)
        return JsonResponse({'qty': cart_quantity})
    else:
        return HttpResponseBadRequest("Invalid request")



def cart_delete(request):
    pass

def cart_update(request):
    pass