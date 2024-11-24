from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label='Enter Address', max_length=255)