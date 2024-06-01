from django.shortcuts import redirect, render
from goods.models import Products
from carts.models import Cart


# Create your views here.
def add_to_cart(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META["HTTP_REFERER"])


def change_in_cart(request, product_): ...


def delete_in_cart(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META["HTTP_REFERER"])
