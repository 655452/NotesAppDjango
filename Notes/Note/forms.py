from django import forms

from .models import *
class NewNote(forms.ModelForm):
    class Meta:
        model=add
        fields=["title","des"]
        labels={"title":"Title","des":"Description"}
