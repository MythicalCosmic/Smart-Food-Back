from rest_framework import serializers
from .models import *

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        fields = ["id", "telegram_id", "username", "phone_number", "telegram_name", "real_name", "latitude", "longitude", "created_at", "updated_at"]

    def create(self, validated_data):
        telegram_id = validated_data.get("telegram_id")
        
        user, created = TelegramUsers.objects.update_or_create(
            telegram_id=telegram_id,
            defaults=validated_data
        )
        return user


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Product
        fields = ["id", "name", "description","category_id", "price", "image", "is_available", "created_at", "updated_at"]
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "order", "name", "created_at", "updated_at"]


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True) 
    product_details = ProductSerializer(source="product", read_only=True) 

    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "product_details", "quantity", "price"]



class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "user", "total_price", "status", "items",  "created_at", "updated_at"]

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(items, many=True).data

    def create(self, validated_data):
        items_data = validated_data.pop("items", []) 
        order = Order.objects.create(**validated_data) 

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data) 
        
        return order