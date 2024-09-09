from django.db import models

class Product(models.Model):
    # Atribut yang diminta oleh tugas
    name = models.CharField(max_length=255)  # Nama item
    price = models.IntegerField()  # Harga item
    description = models.TextField()  # Deskripsi item
    image = models.CharField(max_length=255, default='images/default.avif')  # Gambar produk
    availability = models.CharField(max_length=50, default='In Stock')  # Status ketersediaan
    stock = models.IntegerField(default=0)  # Jumlah stok
    discount = models.CharField(max_length=20, default='No discount')  # Informasi diskon
    

    def __str__(self):
        return self.name  # Mengembalikan nama produk sebagai representasi string

class OwnerInfo(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
