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
        fields = ["id", "name", "created_at", "updated_at"]