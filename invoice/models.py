from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Invoice(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=30,null=True, default=None)
    vendor_name = models.CharField(max_length=30, null=True, default=None)
    date = models.DateField()
    pdf_copy = models.FileField(upload_to='invoice/pdfs/', null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)


class Items(models.Model):
    desc = models.TextField(null=True, default=None)
    qty = models.IntegerField(null=True, default=None)
    rate = models.FloatField(null=True, default=None)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qty + ", " + self.rate


class File(models.Model):
    pdf_copy = models.FileField(upload_to='invoice/pdfs/', null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)