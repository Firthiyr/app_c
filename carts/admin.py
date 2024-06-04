from django.contrib import admin
from carts.models import Cart

# Register your models here.


# admin.site.register(Cart)


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = [
        "product",
        "quantity",
        "created_timestamp",
    ]
    search_fields = [
        "product",
        "quantity",
        "created_timestamp",
    ]
    readonly_fields = [
        "created_timestamp",
    ]
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "user_dispaly",
        "product_dispaly",
        "quantity",
        "created_timestamp",
    ]
    list_filter = [
        "user",
        "product__name",
        "created_timestamp",
    ]

    def user_dispaly(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонімний користувач"

    def product_dispaly(self, obj):
        # create, in order that in the admin in the name of the product there is no quantity.
        return str(obj.product.name)
