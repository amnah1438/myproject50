from django.shortcuts import render
from .models import Product

# 🛒 عرض جميع المنتجات
def product_list(request):
    """
    يعرض قائمة المنتجات من قاعدة البيانات في قالب HTML.
    """
    products = Product.objects.all()  # ✅ جلب جميع المنتجات من قاعدة البيانات
    return render(request, 'store/product_list.html', {'products': products})
