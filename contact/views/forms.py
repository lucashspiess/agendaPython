from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
            }
        ),
        label='Primeiro Nome'
    )
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean(self):
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name
    