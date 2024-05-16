from django.shortcuts import render


# Create your views here.
def catalog(request):
    context = {
        "title": "Home - Каталог",
        "goods": [
            {
                "image": "deps/image/goods/photo_2_2023-04-29_21-57-46-1024x1024.jpg",
                "name": "Nike Air Jordan 1 Retro Low OG ‘Voodoo’",
                "price": "2998₴",
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")