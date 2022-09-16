from bdb import Breakpoint
from xml.dom import ValidationErr
from movieapp.models import reg
from django import forms

class regForm(forms.ModelForm):
    class Meta:
        model=reg
        fields="__all__"

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data['age']
        seat = cleaned_data['seats']
        mobile = str(cleaned_data['mobile'])
        
        if age  <= 0:
            raise forms.ValidationError("Age should not be negative")
        
        if seat  <= 0:
            raise forms.ValidationError("Seat should not be negative")

        if len(mobile) > 10 or len(mobile) < 10:
            raise forms.ValidationError("Invalid mobile number")

        return cleaned_data