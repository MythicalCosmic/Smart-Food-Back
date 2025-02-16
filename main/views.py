from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics 
from rest_framework.permissions import IsAuthenticated 
from rest_framework_api_key.permissions import HasAPIKey
from .custom_responses import CustomResponseMixin
from rest_framework import filters



class TelegramUserCreateView(CustomResponseMixin, generics.CreateAPIView):
    queryset = TelegramUsers.objects.order_by("-id")
    serializer_class = TelegramUserSerializer
    permission_classes = [HasAPIKey]

class TelegramUserRetriveView(CustomResponseMixin, generics.RetrieveAPIView):
    queryset = TelegramUsers.objects.order_by("-id")
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]

class TelegramUserListView(CustomResponseMixin, generics.ListAPIView):
    queryset = TelegramUsers.objects.order_by("-id")
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'telegram_id']


class ProductsListView(CustomResponseMixin, generics.ListAPIView):
    queryset = Product.objects.order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated | HasAPIKey]


class ProductsCreateView(CustomResponseMixin, generics.CreateAPIView):
    queryset = Product.objects.order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    

class ProductUpdateRetrive(CustomResponseMixin, generics.RetrieveUpdateAPIView):
    queryset = Product.objects.order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CategoryListCreateVIew(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Category.objects.order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated | HasAPIKey]

class CategoryUpdateRetriveView(CustomResponseMixin, generics.RetrieveUpdateAPIView):
    queryset = Category.objects.order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]



