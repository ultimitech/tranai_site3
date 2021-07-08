from django import forms
from django.forms import ModelForm
from .models import Document


# create a document form
class DocumentForm(ModelForm):
  class Meta:
    model = Document
    fields = ('dod', 'tod', 'dow', 'title', 'descriptor')
    labels = {
      'dod': 'Date Of Delivery',
      'tod': 'Time Of Day',
      'dow': 'Day Of Week',
      'title': 'Document Title',
      'descriptor': 'Descriptor',
      #  forms.EmailInput(attrs={'class':'form-control'}),
    }

    widgets = {
      # 'dod': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date Of Delivery'}),
      'dod': forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
      'tod': forms.TextInput(attrs={'class':'form-control'}),
      'dow': forms.TextInput(attrs={'class':'form-control'}),
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'descriptor': forms.TextInput(attrs={'class':'form-control'}),
      #  forms.EmailInput(attrs={'class':'form-control'}),
    }