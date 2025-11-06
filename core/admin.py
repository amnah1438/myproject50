from django.contrib import admin

from django.contrib import admin
from .models import UserProfile, SiteSetting

# 🧩 عرض نموذج الملف الشخصي للمستخدم في لوحة التحكم
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'country', 'created_at')
    search_fields = ('user__username', 'phone', 'city', 'country')
    list_filter = ('country',)

# ⚙️ عرض إعدادات الموقع في لوحة التحكم
@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'maintenance_mode', 'updated_at')

