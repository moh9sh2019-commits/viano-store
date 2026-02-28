from django.contrib import admin
from .models import Product # استيراد الموديل الذي أنشأناه سابقاً

admin.site.register(Product)