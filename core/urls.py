from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                  # الصفحة الرئيسية
    path('register/', views.register_view, name='register'),  # إنشاء حساب
    path('login/', views.login_view, name='login'),          # تسجيل الدخول
    path('logout/', views.logout_view, name='logout'),        # تسجيل الخروج
]
