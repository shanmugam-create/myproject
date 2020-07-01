from django import forms
from .models import CustomerTable

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerTable
        fields = ('Name','Gender','Email_Id','Password',)
