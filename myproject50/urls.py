from django.contrib import admin
from django.urls import path, include  # ✅ include لإضافة روابط التطبيقات

urlpatterns = [
    # لوحة الإدارة
    path('admin/', admin.site.urls),

    # 🌟 روابط التطبيقات الثلاثة
    path('', include('core.urls')),        # التطبيق الأساسي (الصفحة الرئيسية مثلاً)
    path('store/', include('store.urls')), # تطبيق المتجر
    path('billing/', include('billing.urls')), # تطبيق الفواتير والدفع
]
