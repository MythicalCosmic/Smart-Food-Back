from django.urls import path  # type: ignore
from .views import *


urlpatterns = [
    path('api/telegram-users/', TelegramUserCreateView.as_view(), name='telegram-user-create'),
    path("api/telegram-users/all", TelegramUserListView.as_view(), name="telegram-user-list"),
    path("api/telegram-users/<int:pk>/", TelegramUserRetriveView.as_view(), name="telegram-user-list"),
    #products
    path("api/products/", ProductsListView.as_view(), name="products-list"),
    path("api/products/create", ProductsCreateView.as_view(), name="products-create"),
    path("api/products/<int:pk>/", ProductUpdateRetrive.as_view(), name="products-update-retrive"),
    #category
    path("api/category/", CategoryListCreateVIew.as_view(), name="category-list-create"),
    path("api/category/<int:pk>/", CategoryUpdateRetriveView.as_view(), name="category-update-retrive"),
    #orders
    path("api/orders/all", OrdersListView.as_view(), name="order-list"),
    path("api/orders/", OrdersCreateView.as_view(), name="order-create"),
    path("api/orders/<int:pk>/", OrdersRetrive.as_view(), name="order-retrive")
]
