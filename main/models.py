from django.db import models

class Product(models.Model):
    nama_identitas = models.TextField()
    kelas_identitas = models.TextField()
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()