from django import forms
from .models import PreparedItem

class PreparedItemForm(forms.ModelForm):
    class Meta:
        model = PreparedItem
        fields = ['title', 'notes', 'prepared_date', 'expiry_date']
