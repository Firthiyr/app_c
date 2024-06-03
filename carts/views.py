from django.shortcuts import render
from goods.models import Products
from carts.models import Cart
from django.http import JsonResponse
from django.template.loader import render_to_string
from carts.utils import get_user_carts
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(
                user=request.user, product=product
            )
            if not created:
                cart.quantity += 1
                cart.save()

        user_cart = get_user_carts(request)
        cart_items_html = render_to_string(
            "carts/includes/cart_included.html", {"carts": user_cart}, request=request
        )

        response_data = {
            "message": "Товар додано до кошику",
            "cart_items_html": cart_items_html,
        }
        return JsonResponse(response_data)
    return JsonResponse({"message": "Метод не поддерживается"}, status=405)


def change_in_cart(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "users/includes/cart_included.html", {"carts": cart}, request=request
    )

    responce_data = {
        "message": "Кількість змінено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(responce_data)


def delete_in_cart(request):

    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/cart_included.html", {"carts": user_cart}, request=request
    )

    responce_data = {
        "message": "Товар видалено",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }
    return JsonResponse(responce_data)
