from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from goods.models import Products


# Create your views here.
def catalog(request, category_slug, page=1):

    page = request.GET.get("page", 1)
    category = request.GET.getlist("category", [])
    manufacturers = request.GET.getlist("manufacturer", [])
    sizes = request.GET.getlist("sizes", [])
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)

    if category_slug == "all-goods":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if category:
        goods = goods.filter(category__slug__in=category)
    if manufacturers:
        goods = goods.filter(brand__slug__in=manufacturers)
    if sizes:
        goods = goods.filter(size__slug__in=sizes)
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by:
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 4)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(
        slug=product_slug
    )  # Получаем инфу о конкретном товаре
    context = {"product": product}

    return render(request, "goods/product.html", context=context)
