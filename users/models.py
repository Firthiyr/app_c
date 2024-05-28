from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Sizes(models.Model):
    image = models.ImageField(upload_to="users_images", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "User"
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
