from django.db import models


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING',
        PAID = 'PAID'
        CANCELLED = 'CANCELLED'

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    product_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return self.full_name
