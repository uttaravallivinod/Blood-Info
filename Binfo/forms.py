from django import forms
from Binfo.models import Blood
class BloodForm(forms.ModelForm):
    class Meta:
        model=Blood
        fields='__all__'
