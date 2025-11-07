from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🧭 لوحة التحكم الإدارية
    path('admin/', admin.site.urls),

    # 🏠 التطبيق الأساسي (core)
    path('', include('core.urls')),

    # 🏪 تطبيق المتجر
    path('store/', include('store.urls')),

    # 💳 تطبيق الفواتير والمدفوعات
    path('billing/', include('billing.urls')),
]

# 🖼️ دعم عرض ملفات الوسائط (Media) أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
