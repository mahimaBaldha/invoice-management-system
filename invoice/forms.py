from django import forms

from .models import Invoice, File


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('pdf_copy',)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('pdf_copy',)