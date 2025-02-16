from django.contrib import admin
from .models import *


admin.site.register(TelegramUsers)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(OrderItem)