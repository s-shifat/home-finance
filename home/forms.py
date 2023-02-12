from django import forms
from .models import Bill, BillTransaction


# Updating bill doesn't work properly. It adds the paid amount

class BillTransactionForm(forms.ModelForm):
    class Meta:
        model = BillTransaction
        fields = ('paid_amount',)
        widgets = {
                'paid_amount': forms.NumberInput(attrs={'class':'form-control'})
        }


    def save(self):
        data = self.cleaned_data
        bill = self.instance.bill
        user = self.instance.paid_by
        paid_amount = data['paid_amount']
        #bill.payers = f"{bill.payers}, {user.username}" if bill.payers else user.username
        #bill.save()
        bill_tx = BillTransaction.objects.create(paid_amount=paid_amount, bill=bill, paid_by=user)


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('amount', 'due_date')
        widgets = {
            'amount': forms.NumberInput(attrs={'class':'form-control', 'type': 'number', 'id':'amount', 'step': '50'}),
            'due_date': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'id':'due-date'}),
    }

