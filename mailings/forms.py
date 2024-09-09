from django import forms
from django.forms import BooleanField

from mailings.models import Mailing, Message, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ('first_send_datetime', 'status')


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
