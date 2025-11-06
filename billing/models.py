from django.db import models
from django.contrib.auth.models import User
from store.models import Order


# 💳 نموذج المدفوعات
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'بطاقة ائتمانية'),
        ('bank_transfer', 'تحويل بنكي'),
        ('cash', 'نقدًا'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="المستخدم"
    )
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name="الطلب"
    )
    amount = models.DecimalField("المبلغ", max_digits=10, decimal_places=2)
    method = models.CharField("طريقة الدفع", max_length=50, choices=PAYMENT_METHODS)
    paid_at = models.DateTimeField("تاريخ الدفع", auto_now_add=True)
    is_successful = models.BooleanField("تم الدفع بنجاح", default=False)

    class Meta:
        verbose_name = "دفعة"
        verbose_name_plural = "المدفوعات"

    def __str__(self):
        return f"دفعة رقم {self.id} - {self.user.username}"


# 🧾 نموذج الفواتير
class Invoice(models.Model):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="invoice",
        verbose_name="الطلب"
    )
    number = models.CharField("رقم الفاتورة", max_length=20, unique=True)
    issue_date = models.DateTimeField("تاريخ الإصدار", auto_now_add=True)
    total_amount = models.DecimalField("إجمالي المبلغ", max_digits=10, decimal_places=2)
    is_paid = models.BooleanField("تم السداد", default=False)

    class Meta:
        verbose_name = "فاتورة"
        verbose_name_plural = "الفواتير"

    def __str__(self):
        return f"فاتورة رقم {self.number}"
