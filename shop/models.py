from django.db import models

class Product(models.Model):
    # التصنيفات التي طلبتها
    CATEGORY_CHOICES = [
        ('ID', 'أيدي'),
        ('BUNDLE', 'حزم'),
    ]
    
    name = models.CharField(max_length=200) # اسم المنتج
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES) # القسم
    price = models.DecimalField(max_digits=10, decimal_places=2) # السعر
    description = models.TextField() # الوصف

    def __str__(self):
        return self.name