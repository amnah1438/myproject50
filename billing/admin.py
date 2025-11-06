from django.contrib import admin

from django.contrib import admin
from .models import Payment, Invoice

# 💳 إدارة المدفوعات
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'amount', 'method', 'is_successful', 'paid_at')
    list_filter = ('method', 'is_successful')
    search_fields = ('user__username', 'order__id')

# 🧾 إدارة الفواتير
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'order', 'total_amount', 'is_paid', 'issue_date')
    list_filter = ('is_paid',)
    search_fields = ('number', 'order__id')

