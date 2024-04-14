from django import forms
from .models import Ilan

class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ["title","content","gender","age","price","phone","address","image"]