from django import forms
from .models import Feedback

class ImageForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback','photo']