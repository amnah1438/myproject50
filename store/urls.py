from django.urls import path
from . import views

app_name = "store"  # 🏷️ لتجنب التعارض بين المسارات

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]
