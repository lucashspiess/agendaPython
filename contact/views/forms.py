from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 'picture'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean(self):
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        error_messages= {
            'required': 'Este campo é obrigatório'
        }
    )

    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', ValidationError('Endereço de e-mail já cadastrado', code='invalid')
            )

        return email