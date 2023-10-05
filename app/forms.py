from django import forms
from app.models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('title', 'cv_file')
