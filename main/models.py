from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    # nama_identitas = models.TextField()
    # kelas_identitas = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()