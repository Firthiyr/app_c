from django.urls import path
from carts import views

app_name = "carts"

urlpatterns = [
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path(
        "change_in_cart/",
        views.change_in_cart,
        name="change_in_cart",
    ),
    path(
        "delete_in_cart/",
        views.delete_in_cart,
        name="delete_in_cart",
    ),
]
