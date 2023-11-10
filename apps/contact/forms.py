from django import forms

from .models import ContactRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'content']

    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here'}),
        required=True
    )
