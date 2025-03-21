from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics 
from rest_framework.permissions import IsAuthenticated 
from rest_framework_api_key.permissions import HasAPIKey
from .custom_responses import CustomResponseMixin
from rest_framework import filters
from rest_framework.response import Response
from .decoraters import GroupPermission
from rest_framework.exceptions import ValidationError



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
    

class OrdersCreateView(CustomResponseMixin, generics.CreateAPIView):
    queryset = Order.objects.order_by("-id")
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items_data = request.data.pop("items", None)
        print(items_data) 
        
        if not items_data:
            raise ValidationError({"items": "This field is required and must contain valid data."})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        for item in items_data:
            item["order"] = order.id
            item_serializer = OrderItemSerializer(data=item)
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()  

        return Response(serializer.data, status=201)





class OrdersRetrive(generics.RetrieveAPIView):
    queryset = Order.objects.order_by("-id")
    serializer_class =  OrderSerializer
    permission_classes = [IsAuthenticated, GroupPermission]