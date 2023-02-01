from django import forms
from .models import Bill, BillTransaction

class BillTransactionForm(forms.ModelForm):
    class Meta:
        model = BillTransaction
        fields = ('paid_amount',)
        widgets = {
                'paid_amount': forms.NumberInput(attrs={'class':'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
