from django.urls import path
from carts import views

app_name = "carts"

urlpatterns = [
    path("add_to_cart/<slug:product_slug>", views.add_to_cart, name="add_to_cart"),
    path(
        "change_in_cart/<slug:product_slug>",
        views.change_in_cart,
        name="change_in_cart",
    ),
    path(
        "delete_in_cart/<slug:product_slug>",
        views.delete_in_cart,
        name="delete_in_cart",
    ),
]
