from django.contrib import admin

from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# 🏷️ إدارة الفئات
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# 🛍️ إدارة المنتجات
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

# 📦 إدارة الطلبات
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username',)

# 🧾 إدارة عناصر الطلب
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

