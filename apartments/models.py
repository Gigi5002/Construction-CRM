from django.db import models


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('reserved', 'Бронь'),
        ('sold', 'Куплено'),
        ('installment', 'Рассрочка'),
        ('barter', 'Бартер'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    # Необязательные поля
    floor = models.IntegerField(null=True, blank=True)
    object_name = models.CharField(max_length=100, null=True, blank=True)
    square_meters = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
