from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Brands(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Brand"
        verbose_name = "Бренд"
        verbose_name_plural = "Бренди"


class Sizes(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Size"
        verbose_name = "Розмір"
        verbose_name_plural = "Розміри"


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    category = models.ForeignKey(
        to=Categories,
        verbose_name="Категорія",
        related_name="products",
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        to=Brands,
        verbose_name="Бренди",
        related_name="products",
        on_delete=models.CASCADE,
    )
    size = models.ManyToManyField(
        Sizes, verbose_name="Розміри", related_name="products"
    )
    image = models.ImageField(
        upload_to="products", blank=True, null=True, verbose_name="Зображення"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=0, verbose_name="Ціна у %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.name} Кількість - {self.quantity}"

    def display_id(self):
        return f"{self.id:04}"

    def sell_price(self):
        if self.discount:  # Проработка скидки на сайте
            return round(self.price - self.price * self.discount / 100, 2)
        return (
            self.price
        )  # Если скидки нет возв. обычная цена, если есть уже со скидкой

    class Meta:
        db_table = "Product"
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ("id",)
