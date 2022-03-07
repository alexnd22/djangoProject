from django.db import models

from category.models import Category


class Product(models.Model):
    stock_choices = (('yes', 'Yes'), ('no', 'No'))

    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_stock = models.CharField(max_length=10, choices=stock_choices, null=True, blank=True)
    release = models.DateField(null=True, blank=True)
    # email = models.EmailField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.name
