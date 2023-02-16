from django import forms
from .models import Category, Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['item_name', 'cost', 'category']
        widgets = {
                'item_name': forms.TextInput(attrs={'class':'form-control'}),
                'cost': forms.NumberInput(attrs={'class':'form-control', 'step': '1'}),
                'category': forms.Select(attrs={'class': 'form-control'})
        }
    
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['category'].widget.attrs.update({'class': 'form-control'})
#        print('category--------',self.fields['category'].widget)



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
                'item_name': forms.TextInput(attrs={'class':'form-control'}),
                'description': forms.TextInput(attrs={'class':'form-control'}),
        }

