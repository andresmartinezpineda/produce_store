from django.db import models
from shop_admin.models import Product
from django.contrib.auth.models import User
from django.utils import timezone

class Sale(models.Model):
    """
    Represents a sale transaction made by a user.
    Stores the user who made the sale, the date, and the total amount.
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE) # User who performed the sale
    date = models.DateTimeField(default=timezone.now) # Date and time of the sale
    total = models.DecimalField(max_digits=10,decimal_places=2) # Total amount of the sale

    def __str__(self):
        return f"sale # {self.id} - {self.date.date()}"
    

class SaleItem(models.Model):
    """
    Represents a product included in a specific sale.
    Stores product details, quantity sold, and price at the time of sale.
    """
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE,related_name='items') # Sale to which this item belongs
    product = models.ForeignKey(Product,on_delete=models.CASCADE) # Product sold
    quantity = models.DecimalField(max_digits=10,decimal_places=2) # Quantity sold
    price = models.DecimalField(max_digits=10,decimal_places=2) # Price per unit at the time of sale

    def subtotal(self):
        """
        Returns the subtotal amount for this product (quantity * price).
        """
        return self.quantity * self.price