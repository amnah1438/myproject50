from django.urls import path
from . import views  # ✅ استدعاء ملف العرض (views.py)

urlpatterns = [
    path('', views.home, name='home'),  # الصفحة الرئيسية
]

