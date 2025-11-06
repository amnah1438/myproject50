from django.db import models

from django.db import models
from django.contrib.auth.models import User
from store.models import Order

# 💳 المدفوعات
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'بطاقة ائتمانية'),
        ('bank_transfer', 'تحويل بنكي'),
        ('cash', 'نقدًا'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    paid_at = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment #{self.id} - {self.user.username}"

# 🧾 الفواتير
class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="invoice")
    number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.number}"

