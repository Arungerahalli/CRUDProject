from django import forms
from CRUDApp.models import CRUDApp_StudentTable

class CRUDApp_StudentTableForm(forms.ModelForm):
    class Meta:
        model=CRUDApp_StudentTable
        fields='__all__'