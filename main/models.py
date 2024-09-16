from django.db import models
import uuid

class Product(models.Model):
    # Atribut yang diminta oleh tugas
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    availability = models.CharField(max_length=50, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')])
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.name  # Mengembalikan nama produk sebagai representasi string

class OwnerInfo(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
