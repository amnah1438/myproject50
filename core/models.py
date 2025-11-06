from django.db import models
from django.contrib.auth.models import User


# 🧩 نموذج لتخزين معلومات إضافية عن المستخدم
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="المستخدم"
    )
    phone = models.CharField("رقم الجوال", max_length=20, blank=True, null=True)
    address = models.CharField("العنوان", max_length=255, blank=True, null=True)
    city = models.CharField("المدينة", max_length=100, blank=True, null=True)
    country = models.CharField("الدولة", max_length=100, blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)

    class Meta:
        verbose_name = "الملف الشخصي للمستخدم"
        verbose_name_plural = "الملفات الشخصية للمستخدمين"

    def __str__(self):
        return self.user.username


# ⚙️ نموذج للإعدادات العامة للنظام
class SiteSetting(models.Model):
    site_name = models.CharField("اسم الموقع", max_length=150)
    maintenance_mode = models.BooleanField("وضع الصيانة", default=False)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name
