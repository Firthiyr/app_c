from django.shortcuts import render, get_list_or_404
from goods.models import Products


# Create your views here.
def catalog(request, category_slug):

    if category_slug == "all-goods":
        goods = (
            Products.objects.all()
        )  # При росте сайта, писать тут лучше чем в контекст.
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(
        slug=product_slug
    )  # Получаем инфу о конкретном товаре
    context = {"product": product}

    return render(request, "goods/product.html", context=context)
