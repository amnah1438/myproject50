from django.db import models
from django.db import models
from django.contrib.auth.models import User

# 🧩 نموذج لتخزين معلومات إضافية عن المستخدم
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# ⚙️ نموذج للإعدادات العامة للنظام
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=150)
    maintenance_mode = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

