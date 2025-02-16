from django.db import models

class TelegramUsers(models.Model):
    telegram_id = models.IntegerField()
    username = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=30)
    telegram_name = models.CharField(max_length=255)
    real_name = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Telegram Id: {self.telegram_id} - Username: {self.username} - Full Name: {self.telegram_name}"
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to="products/", blank=True, null=True)  
    is_available = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("preparing", "Preparing"),
        ("out_for_delivery", "Out for Delivery"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(TelegramUsers, on_delete=models.CASCADE)  
    products = models.ManyToManyField("Product", through="OrderItem") 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending") 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Order {self.id} - {self.user.telegram_id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Order {self.order.id})"
