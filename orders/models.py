from django.db import models
from goods.models import Products
from users.models import User


# Create your models here.


class OrderitemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, verbose_name="Користувач", default=None
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення"
    )
    phone_number = models.CharField(max_length=13, verbose_name="Номер теелфону")
    requires_delivery = models.BooleanField(
        default=False, verbose_name="Потріба доставка"
    )
    delivery_address = models.TextField(
        null=True, blank=True, verbose_name="Адреса доставки"
    )
    payment_on_get = models.BooleanField(
        default=False, verbose_name="Оплата при отриманні"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Сплачено")
    status = models.CharField(
        max_length=50, default="В обробці", verbose_name="Статус замолвення"
    )

    def __str__(self):
        return f"Замолвення № {self.pk} | Покупець {self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = "Order"
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, verbose_name="Замолвення"
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.SET_DEFAULT,
        null=True,
        verbose_name="Товар",
        default=None,
    )
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата продажу"
    )

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Замовлення № {self.order.pk}"

    class Meta:
        db_table = "Order item"
        verbose_name = "Проданий товар"
        verbose_name_plural = "Продані товари"
