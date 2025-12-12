from django import forms
from .models import TextoSobre

class AboutForm(forms.Form):  # <-- ¡Asegúrate de que el nombre coincida!
    texto = forms.CharField(widget=forms.Textarea)

