from django.shortcuts import render
from .models import Product

def home(request):
    # جلب كل المنتجات من قاعدة البيانات
    all_products = Product.objects.all()
    # إرسالها لملف الـ HTML
    return render(request, 'shop/home.html', {'products': all_products})
