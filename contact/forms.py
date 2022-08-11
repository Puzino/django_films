from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по почте"""

    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Your Email...'})
        }
        labels = {
            'email': ''
        }
