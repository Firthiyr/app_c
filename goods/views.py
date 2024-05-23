from django.shortcuts import render
from goods.models import Products


# Create your views here.
def catalog(request):

    goods = Products.objects.all()  # При росте сайта, писать тут лучше чем в контекст.
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
