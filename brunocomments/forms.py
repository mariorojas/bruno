from django import forms
from django.utils.translation import gettext as _

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']
        error_messages = {
            'author': {
                'required': _('Este campo es obligatorio'),
                'max_length': _(
                    'Asegúrate que tu mensaje no exceda %(limit_value)d '
                    'caracteres de longitud, actualmente tiene %(show_value)d.')
            },
            'comment': {
                'required': _('Este campo es obligatorio'),
                'max_length': _(
                    'Asegúrate que tu mensaje no exceda %(limit_value)d '
                    'caracteres de longitud, actualmente tiene %(show_value)d.')
            }
        }
