from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics 
from rest_framework.permissions import IsAuthenticated 
from rest_framework_api_key.permissions import HasAPIKey
from .custom_responses import CustomResponseMixin
from rest_framework import filters
from .decoraters import GroupPermission


#Telegram User Actions
class TelegramUserCreateView(CustomResponseMixin, generics.CreateAPIView):
    queryset = TelegramUsers.objects.order_by("-id")
    serializer_class = TelegramUserSerializer
    permission_classes = [HasAPIKey]

class TelegramUserRetriveView(CustomResponseMixin, generics.RetrieveAPIView):
    queryset = TelegramUsers.objects.order_by("-id")
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]

class TelegramUserListView(generics.ListAPIView):
    queryset = TelegramUsers.objects.order_by("-id")
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'telegram_id']




#Product Actions
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



#Category Actions
class CategoryListCreateVIew(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Category.objects.order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated | HasAPIKey]

class CategoryUpdateRetriveView(CustomResponseMixin, generics.RetrieveUpdateAPIView):
    queryset = Category.objects.order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]



#Orders Actions
class OrdersListView(generics.ListAPIView):
    queryset = Order.objects.order_by("-id")
    serializer_class =  OrderSerializer
    permission_classes = [IsAuthenticated]

class OrdersCreateView(generics.CreateAPIView):
    queryset = Order.objects.order_by("-id")
    serializer_class =  OrderSerializer
    permission_classes = [HasAPIKey]


class OrdersRetrive(generics.RetrieveAPIView):
    queryset = Order.objects.order_by("-id")
    serializer_class =  OrderSerializer
    permission_classes = [IsAuthenticated, GroupPermission]