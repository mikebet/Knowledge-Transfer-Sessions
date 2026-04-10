from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    id = forms.CharField(max_length=50, required=True)
    phone = forms.CharField(max_length=20, required=True)
