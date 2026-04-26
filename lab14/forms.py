from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Түсініктеме жазатын форма.
    ModelForm Django-ның дайын валидациясын пайдаланады.
    """
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={
                'placeholder': 'Атыңызды жазыңыз',
                'class': 'form-input',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Түсініктемеңізді жазыңыз... (<script> тегін де жазып көріңіз)',
                'rows': 4,
                'class': 'form-input',
            }),
        }
        labels = {
            'author': 'Автор',
            'content': 'Мазмұн',
        }
