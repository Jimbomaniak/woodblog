from django.forms import ModelForm, Textarea
from .models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        exclude = ['comments_article', 'pub_date']
        widgets = {
            'comments_text': Textarea(attrs={
                'cols': '100%',
                'rows': 3,
                'placeholder': 'введите текст'
            })
        }
        labels = {
            'comments_text': '',
        }
