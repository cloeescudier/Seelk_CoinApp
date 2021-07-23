from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Alert(models.Model):
    name = models.CharField(max_length=255, default="Alert")
    message = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    activated = models.BooleanField(default=True)

    crypto = models.CharField(max_length=3, default="BTC")
    currency = models.CharField(max_length=3, default="USD")

    user = models.ForeignKey('User', null=False, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    email = models.EmailField(default="example@gmail.com")

class ValueAlert(Alert):
    value = models.DecimalField(max_digits=30, decimal_places=10)

    choices = (
        ('A', 'Above'),
        ('B', 'Below'),
    )
    direction = models.CharField(max_length=1, choices=choices)
    


class PercentageAlert(Alert):
    timeframe = models.DurationField()
    percentage = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    choices = (
        ('U', 'Up'),
        ('D', 'Down'),
    )
    direction = models.CharField(max_length=1, choices=choices)