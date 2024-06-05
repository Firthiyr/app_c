from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "User"
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
