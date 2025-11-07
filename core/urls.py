from django.urls import path
from . import views

app_name = "core"  # 🔖 لتجنّب التعارض مع تطبيقات أخرى مستقبلاً

urlpatterns = [
    # 🏠 الصفحة الرئيسية
    path('', views.home, name='home'),

    # 🧩 إنشاء حساب جديد
    path('register/', views.register_view, name='register'),

    # 🔐 تسجيل الدخول
    path('login/', views.login_view, name='login'),

    # 🚪 تسجيل الخروج
    path('logout/', views.logout_view, name='logout'),
]
