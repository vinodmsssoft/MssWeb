from django import forms
from webApp.models import Contact



class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(label="Company", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label="Subject", widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.IntegerField(label="Contact", widget=forms.NumberInput(attrs={'class':'form-control'}))
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
    class Meta:
        model =Contact
        fields = '__all__'


