from django import forms
from .models import Users

class Users_forms(forms.ModelForm):
    class Meta:
        model=Users
        fields=['first_name','last_name','age','email_address'] 
        

