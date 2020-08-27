from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re

def validate_name(name):
    m=re.match('[a-zA-Z]+',name)
    if m.group()!= name:
        raise ValidationError("Name is Not found")
    return name

class SampleForm(forms.Form):
    name= forms.CharField(max_length=200,required=True,label='Name:',validators=[validate_name])
    email= forms.EmailField(max_length=100, required=True, label="Email:",validators=[validators.MinLengthValidator(10)])
    confirm_email= forms.EmailField(max_length=100, required=True,label="Confirm Email")
    ip_address= forms.CharField(max_length=100, required=True,validators=[validators.validate_ipv4_address])
    pwd= forms.CharField(max_length=200, required=True,label="Password:",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    profile_pic= forms.ImageField(max_length=200, required=True, label="Profile Pic:")

    def clean(self,*args, **kwargs):
        cleaned_data= super().clean()
        email= cleaned_data.get('email')
        cemail= cleaned_data.get('confirm_email')
        if email == cemail:
            return cleaned_data
        self.add_error('confirm_email',"Both emails are not same")

#def clean(self,*args, **kwargs):
#       cleaned_data= super().clean()
#        email= cleaned_data.get('email')
#        cemail= cleaned_data.get('confirm_email')
#        if email != cemail:
#            raise ValidationError("emails are not same")
#        return cleaned_data