from django.contrib import admin
from goods.models import Categories, Products, Brands, Sizes

# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Products)
# admin.site.register(Brands)
# admin.site.register(Sizes)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Sizes)
class SizesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
