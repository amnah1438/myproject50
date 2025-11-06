from django.db import models
from django.contrib.auth.models import User

# 🏷️ الفئات
class Category(models.Model):
    name = models.CharField("اسم الفئة", max_length=100)
    description = models.TextField("الوصف", blank=True, null=True)

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name


# 🛍️ المنتجات
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="الفئة")
    name = models.CharField("اسم المنتج", max_length=150)
    description = models.TextField("الوصف")
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("الكمية المتوفرة", default=0)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    image = models.ImageField("صورة المنتج", upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


# 📦 الطلبات
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="المستخدم")
    created_at = models.DateTimeField("تاريخ الطلب", auto_now_add=True)
    status = models.CharField("حالة الطلب", max_length=50, default='قيد المعالجة')

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"الطلب رقم {self.id} - {self.user.username}"


# 🧾 عناصر الطلب
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField("الكمية", default=1)
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
