from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
#    category = models.CharField(max_length=30) ForeignKey()
    in_stock = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self): # Возвращает список в следующем формате, если используется filter
        return f'Product(id:{self.pk} title:{self.title} price:{self.price} created_at:{self.created_at}'
    def __str__(self): # Возвращает список в следующем формате, если используется get
        return f'Product(title:{self.title} price:{self.price} created_at:{self.created_at}'

