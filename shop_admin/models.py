from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    #Represents a product category for classification purposes. Example: Fruits, Vegetables, Grains, etc.
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name
    

class Product(models.Model):
    # Represents a product available in the Fruver inventory. Includes details such as name, description, price, stock, unit of measurement, and category.
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit or kilogram")
    stock = models.DecimalField(max_digits=10, decimal_places=2, help_text="Inventory quantity (could be in kg, units, etc.)")
    unit = models.CharField(max_length=50, choices=[
        ('Kg', 'Kilograms'),
        ('Unit', 'Unit'),
        ('Bag', 'Bag'),
        ('Pound', 'Pound'),
        ('Box', 'Box'),
    ], default='Kg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.unit}) - Stock: {self.stock}"
