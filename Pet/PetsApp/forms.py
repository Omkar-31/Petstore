from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = BillingDetail
        fields = ['fname','lname','building','add1','add2','city','state','pincode']
        