from django.shortcuts import render
from .models import Product

# 🛍️ عرض قائمة المنتجات
def product_list(request):
    """
    دالة تعرض جميع المنتجات الموجودة في قاعدة البيانات.
    """
    products = Product.objects.all()  # جلب كل المنتجات
    return render(request, 'store_templates/product_list.html', {'products': products})
