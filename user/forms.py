from django import forms
from .models import Profile

class StudentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "email", "image",]
        